from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf import settings
import work.views

urlpatterns = [
    url(r'^my-dashboard/$', work.views.my_dashboard, name="my_dashboard"),
    url(r'^non-process-logging/$', work.views.non_process_logging, name="non_process_logging"),
    url(r'^work-timer/(?P<process_id>\d+)/(?P<commitment_id>\d+)/$', work.views.work_timer, name="work_timer"),
    url(r'^process-logging/(?P<process_id>\d+)/$', work.views.process_logging, name="process_logging"),
    url(r'^work-process-finished/(?P<process_id>\d+)/$', work.views.work_process_finished, name="work_process_finished"),
    url(r'^order-list/$', work.views.order_list, name="order_list"),
    url(r'^order-plan/(?P<order_id>\d+)/$', work.views.order_plan, name="order_plan"),
    url(r'^change-project-order/(?P<order_id>\d+)/$', work.views.change_project_order, name="change_project_order"),
    url(r"^plan-work/(?P<rand>\d+)/$", work.views.plan_work, name="plan_work"),
    url(r"^order-delete-confirmation-work/(?P<order_id>\d+)/$", work.views.order_delete_confirmation_work, name="order_delete_confirmation_work"),
    url(r'^my-history/$', work.views.my_history, name="my_history"),
    url(r'^work-home/$', work.views.work_home, name="work_home"),
    url(r'^save-timed-work-now/(?P<event_id>\d+)/$', work.views.save_timed_work_now, name="save_timed_work_now"),
    url(r'^change-history-event/(?P<event_id>\d+)/$', work.views.change_history_event, name="change_history_event"),
    url(r'^map/$', work.views.map, name="map"),
    url(r'^project-work/$', work.views.project_work, name="project_work"),
    url(r'^agent/(?P<agent_id>\d+)/exchanges/$', work.views.exchanges_all, name="exchanges_all"),
    url(r'^agent/(?P<context_agent_id>\d+)/exchange-logging-work/(?P<exchange_type_id>\d+)/(?P<exchange_id>\d+)/$', work.views.exchange_logging_work,
        name="exchange_logging_work"),

    url(r'^profile/$', work.views.profile, name="profile"),
    url(r'^change-personal-info/(?P<agent_id>\d+)/$', work.views.change_personal_info, name="change_personal_info"),
    url(r'^upload-picture/(?P<agent_id>\d+)/$', work.views.upload_picture, name="upload_picture"),
    url(r'^update-skills/(?P<agent_id>\d+)/$', work.views.update_skills, name="update_skills"),
    url(r"^add-worker-to-location/(?P<location_id>\d+)/(?P<agent_id>\d+)/$", work.views.add_worker_to_location, name="add_worker_to_location"),
    url(r"^add-location-to-worker/(?P<agent_id>\d+)/$", work.views.add_location_to_worker, name="add_location_to_worker"),
    url(r'^membership-discussion/(?P<membership_request_id>\d+)/$', work.views.membership_discussion,
        name="membership_discussion"),

    url(r"^work-add-todo/$", work.views.work_add_todo, name="work_add_todo"),
    url(r"^work-todo-done/(?P<todo_id>\d+)/$", work.views.work_todo_done, name="work_todo_done"),
    url(r"^work-todo-time/$", work.views.work_todo_time, name="work_todo_time"),
    url(r"^work-todo-description/$", work.views.work_todo_description, name="work_todo_description"),
    url(r"^work-todo-decline/(?P<todo_id>\d+)/$", work.views.work_todo_decline, name="work_todo_decline"),
    url(r"^work-todo-mine/(?P<todo_id>\d+)/$", work.views.work_todo_mine, name="work_todo_mine"),
    url(r"^work-todo-change/(?P<todo_id>\d+)/$", work.views.work_todo_change, name="work_todo_change"),
    url(r"^work-todo-delete/(?P<todo_id>\d+)/$", work.views.work_todo_delete, name="work_todo_delete"),
    url(r"^work-commit-to-task/(?P<commitment_id>\d+)/$", work.views.work_commit_to_task,
        name="work_commit_to_task"),
    url(r"^work-delete-event/(?P<event_id>\d+)/$", work.views.work_delete_event,
        name="work_delete_event"),

    # bum2
    url(r"^your-projects/$", work.views.your_projects, name="your_projects"),
    url(r"^agent/(?P<agent_id>\d+)/$", work.views.members_agent, name="members_agent"),
    url(r"^agent/(?P<agent_id>\d+)/join-requests/$", work.views.join_requests, name="join_requests"),
    #url(r"^agent/(?P<agent_id>\d+)/create-user-agent/$", work.views.create_project_user_and_agent, name="create_project_user_and_agent"),
    url(r'^assign-skills/(?P<agent_id>\d+)/$', work.views.assign_skills, name="assign_skills"),
    url(r'^new_skill_type/(?P<agent_id>\d+)/$', work.views.new_skill_type, name="new_skill_type"),
    url(r'^my-tasks/$', work.views.my_tasks, name="my_tasks"),
    url(r'^take-new-tasks/$', work.views.take_new_tasks, name="take_new_tasks"),
    url(r'^home/$', work.views.my_dashboard, name="home"),
    url(r"^create-your-project/$", work.views.create_your_project, name="create_your_project"),
    url(r"^change-your-project/(?P<agent_id>\d+)/$", work.views.change_your_project, name="change_your_project"),
    url(r'^project-feedback/(?P<agent_id>\d+)/(?P<join_request_id>\d+)/$', work.views.project_feedback,
        name="project_feedback"),
    url(r'^joinaproject/(?P<agent_id>\d+)/(?P<join_request_id>\d+)/$', work.views.project_feedback,
        name="joinaproject"),
    url(r'^agent/(?P<agent_id>\d+)/project_joinform/$', work.views.joinaproject_request_internal,
        name="project_joinform"),
    url(r"^edit-relations/(?P<agent_id>\d+)/$", work.views.edit_relations, name="edit_relations"),
    url(r'^join-project/(?P<project_id>\d+)/$', work.views.join_project,
        name="join_project"),

    url(r'^connect-agent-to-join-request/(?P<agent_id>\d+)/(?P<join_request_id>\d+)/$', work.views.connect_agent_to_join_request,
        name="connect_agent_to_join_request"),
    #url(r'^create-agent-for-join-request/(?P<agent_id>\d+)/(?P<join_request_id>\d+)/$', work.views.create_agent_for_join_request,
    #    name="create_agent_for_join_request"),

    url(r'^accept-request/(?P<join_request_id>\d+)/$', work.views.accept_request,
        name="accept_request"),
    url(r'^decline-request/(?P<join_request_id>\d+)/$', work.views.decline_request,
        name="decline_request"),
    url(r'^undecline-request/(?P<join_request_id>\d+)/$', work.views.undecline_request,
        name="undecline_request"),
    url(r'^delete-request/(?P<join_request_id>\d+)/$', work.views.delete_request,
        name="delete_request"),
    url(r'^create-ocp-acount/(?P<join_request_id>\d+)/$', work.views.create_account_for_join_request,
        name="create_account_for_join_request"),
    url(r"^comments/$", work.views.comments, name="comments"),

    url(r'^payment-url/(?P<paymode>.+)/(?P<join_request_id>\d+)/$', work.views.payment_url, name="payment_url"),

    url(r'^share-payment/(?P<agent_id>\d+)/$', work.views.share_payment, name="share_payment"),
    url(r"^validate-nick/$", work.views.validate_nick, name="validate_nick"),
    url(r"^validate-username/$", work.views.validate_username, name="validate_username"),
    url(r'^new-features/$', work.views.new_features, name='new_features'),

    url(r"^invoice-number/$", work.views.invoice_number, name="invoice_number"),

    url(r"^agent/(?P<agent_id>\d+)/resources/$", work.views.project_all_resources, name="project_resources"),
    url(r"^agent/(?P<agent_id>\d+)/resources/(?P<resource_id>\d+)/$", work.views.project_resource, name="project_resource"),
    url(r"^agent/(?P<agent_id>\d+)/resources/new/(?P<Rtype>[\w-]+)/$", work.views.new_resource_type, name="new_resource_type"),
    url(r"^agent/(?P<agent_id>\d+)/change-resource/(?P<resource_id>\d+)/$", work.views.change_resource, name="change_resource"),


    url(r'^add-transfer/(?P<exchange_id>\d+)/(?P<transfer_type_id>\d+)/$', work.views.add_transfer,
        name="add_transfer"),
    url(r'^add-transfer-commitment-work/(?P<exchange_id>\d+)/(?P<transfer_type_id>\d+)/$', work.views.add_transfer_commitment_work,
        name="add_transfer_commitment_work"),
    url(r'^change-transfer-commitments-work/(?P<transfer_id>\d+)/$', work.views.change_transfer_commitments_work,
        name="change_transfer_commitments_work"),
    url(r'^delete-transfer-commitments/(?P<transfer_id>\d+)/$', work.views.delete_transfer_commitments,
        name="delete_transfer_commitments"),
    url(r'^transfer-from-commitment/(?P<transfer_id>\d+)/$', work.views.transfer_from_commitment,
        name="transfer_from_commitment"),
    url(r'^change-transfer-events/(?P<transfer_id>\d+)/(?P<context_agent_id>\d+)/$', work.views.change_transfer_events_work,
        name="change_transfer_events_work"),
    url(r'^delete-transfer-events/(?P<transfer_id>\d+)/$', work.views.delete_transfer_events,
        name="delete_transfer_events"),

    url(r'^add-work-for-exchange/(?P<exchange_id>\d+)/$', work.views.add_work_for_exchange,
        name="add_work_for_exchange"),
    url(r'^change-exchange-work-event/(?P<event_id>\d+)/$', work.views.change_exchange_work_event,
        name="change_exchange_work_event"),
    url(r"^delete-event/(?P<event_id>\d+)/$", work.views.work_delete_event,
        name="work_delete_event"),

    url(r'^delete-exchange/(?P<exchange_id>\d+)/$', work.views.delete_exchange,
        name="delete_exchange"),

    url(r'^add-transfer-external-agent/(?P<commitment_id>\d+)/(?P<context_agent_id>\d+)/$', work.views.add_transfer_external_agent,
        name="add_transfer_external_agent"),

    url(r"^json-resourcetype-resources-locations/(?P<ocp_artwork_type_id>\d+)/$", work.views.json_ocp_resource_type_resources_with_locations,
        name="json_ocp_resource_type_resources_with_locations"),
    url(r"^work-change-process-sked-ajax/$", work.views.work_change_process_sked_ajax,
        name="work_change_process_sked_ajax"),
    url(r"^work-change-process/(?P<process_id>\d+)/$", work.views.work_change_process,
        name="work_change_process"),

    url(r"^project-history/(?P<agent_id>\d+)/$", work.views.project_history, name="project_history"),
    url(r'^project-history-csv/$', work.views.project_history_csv,
        name="project_history_csv"),

    url(r'^work-log-resource/(?P<commitment_id>\d+)/$', work.views.work_log_resource_for_commitment,
        name="work_log_resource_for_commitment"),
    url(r"^work-uncommit/(?P<commitment_id>\d+)/$", work.views.work_uncommit,
        name="work_uncommit"),
    url(r"^work-add-process-worker/(?P<process_id>\d+)/$", work.views.work_add_process_worker,
        name="work_add_process_worker"),
    url(r"^work-invite-collaborator/(?P<commitment_id>\d+)/$", work.views.work_invite_collaborator,
        name="work_invite_collaborator"),
    url(r"^work-change-commitment/(?P<commitment_id>\d+)/$", work.views.work_change_commitment,
        name="work_change_commitment"),
    url(r'^work-add-to-resource/(?P<commitment_id>\d+)/$', work.views.work_add_to_resource_for_commitment,
        name="work_add_to_resource_for_commitment"),
    url(r'^work-event/(?P<commitment_id>\d+)/$', work.views.work_add_work_event,
        name="work_add_work_event"),
    url(r"^change-work-event/(?P<event_id>\d+)/$", work.views.work_change_work_event,
        name="work_change_work_event"),
    url(r"^add-process-input/(?P<process_id>\d+)/(?P<slot>\w{1})/$", work.views.work_add_process_input,
        name="work_add_process_input"),
    url(r"^json-directional-unit/(?P<resource_type_id>\d+)/(?P<direction>\w+)/$", work.views.work_json_directional_unit,
        name="work_json_directional_unit"),
    url(r"^delete-process-commitment/(?P<commitment_id>\d+)/$", work.views.work_delete_process_commitment,
        name="work_delete_process_commitment"),
    url(r'^unplanned-work-event/(?P<process_id>\d+)/$', work.views.work_add_unplanned_work_event,
        name="work_add_unplanned_work_event"),
    url(r"^change-unplanned-work-event/(?P<event_id>\d+)/$", work.views.work_change_unplanned_work_event,
        name="work_change_unplanned_work_event"),
    url(r'^unplanned-output-event/(?P<process_id>\d+)/$', work.views.work_add_unplanned_output,
        name="work_add_unplanned_output"),
    url(r'^unplanned-input-event/(?P<process_id>\d+)/(?P<slot>\w{1})/$', work.views.work_add_unplanned_input_event,
        name="work_add_unplanned_input_event"),
    url(r"^json-resourcetype-resources/(?P<resource_type_id>\d+)/$", work.views.json_resource_type_resources,
        name="work_json_resource_type_resources"),
    url(r'^consumption-event/(?P<commitment_id>\d+)/(?P<resource_id>\d+)/$', work.views.work_add_consumption_event,
        name="work_add_consumption_event"),
    url(r"^add-process-output/(?P<process_id>\d+)/$", work.views.work_add_process_output,
        name="work_add_process_output"),
    url(r'^use-event/(?P<commitment_id>\d+)/(?P<resource_id>\d+)/$', work.views.work_add_use_event,
        name="work_add_use_event"),
    url(r"^log-stage-change-event/(?P<commitment_id>\d+)/(?P<resource_id>\d+)/$", work.views.work_log_stage_change_event,
        name="work_log_stage_change_event"),
    url(r"^add-process-citation/(?P<process_id>\d+)/$", work.views.work_add_process_citation,
        name="work_add_process_citation"),
    url(r'^citation-event/(?P<commitment_id>\d+)/(?P<resource_id>\d+)/$', work.views.work_add_citation_event,
        name="work_add_citation_event"),
    url(r'^unplanned-cite-event/(?P<process_id>\d+)/$', work.views.work_add_unplanned_cite_event,
        name="work_add_unplanned_cite_event"),
    url(r"^delete-citation-event/(?P<commitment_id>\d+)/(?P<resource_id>\d+)/$", work.views.work_delete_citation_event,
        name="work_delete_citation_event"),
    url(r"^json-citation-unit/(?P<resource_type_id>\d+)/$", work.views.json_resource_type_citation_unit,
        name="work_json_resource_type_citation_unit"),
    url(r"^join-task/(?P<commitment_id>\d+)/$", work.views.work_join_task,
        name="work_join_task"),
    url(r"^json-context-resource_types/(?P<context_id>\d+)/(?P<pattern_id>\d+)/$", work.views.json_get_context_resource_types,
        name="work_json_get_context_resource_types"),
]
