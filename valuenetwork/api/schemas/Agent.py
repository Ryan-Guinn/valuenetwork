#
# Graphene schema for exposing EconomicAgent model
#
# @package: OCP
# @author:  pospi <pospi@spadgos.com>
# @since:   2017-03-20
#

from django.core.exceptions import PermissionDenied

import graphene
from graphene_django.types import DjangoObjectType

from valuenetwork.valueaccounting.models import EconomicAgent, AgentUser
from valuenetwork.api.schemas.helpers import *

# bind Django models to Graphene types


class Agent(DjangoObjectType):
    image = graphene.String(source='image')
    class Meta:
        model = EconomicAgent
        only_fields = ('id', 'name', 'description', 'url')


# define public query API

class Query(graphene.AbstractType):

    # define input query params

    agent = graphene.Field(Agent,
                           me=graphene.Boolean())

    all_agents = graphene.List(Agent)

    my_organizations = graphene.List(Agent,
                                     me=graphene.Boolean())
    
    organization_members = graphene.List(Agent,
                                         id=graphene.Int())    

    # load single agents

    def _load_own_agent(self):
        agentUser = AgentUser.objects.filter(user=self.user).first()
        if agentUser is None:
            raise PermissionDenied("Cannot find requested user")
        return agentUser.agent

    def resolve_agent(self, args, *rargs):
        me = args.get('me')

        # load own agent

        if (me is not None):
            return self._load_own_agent()

    # load agents list

    def resolve_all_agents(self, args, context, info):
        return EconomicAgent.objects.all()

    # load context agents that 'me' is related to with 'member' or 'manager' behavior
    # (this gives the projects, collectives, groups that the user agent is any
    # kind of member of)

    def resolve_my_organizations(self, args, context, info):
        my_agent = self._load_own_agent()
        return my_agent.is_member_of()
    
    # load members of an organization (context agent)

    def resolve_organization_members(self, args, context, info):
        id = args.get('id')
        if id is not None:
            org = EconomicAgent.objects.get(pk=id)
            if org:
                return org.members()
        return None
