from django.urls import path
from run.views import run3,run2,run,extract_block_names,extract_programs_for_block,get_latest_project_setup,get_latest_build_path,get_project_list,execute_commands,extract_project_names,extract_blocks_for_project,redirect_dashboard

urlpatterns = [
    path('', run,name="run"),
    path('2/',run2,name='run2'),
    path('3/',run3,name='run3'),
    path('get_blocks/', extract_block_names, name='get_blocks'),
    path('get_blocks/<str:project_name>/', extract_blocks_for_project, name='get_blocks_for_project'),
    path('get_all_projects/', extract_project_names, name='get-projects'),
    path('get_projects/<str:block_name>/', extract_programs_for_block, name='get_programs_for_block'),
    path('get_project_setups/<str:project>/', get_latest_project_setup, name='get_latest_project_setup'),
    path('get_latest_build_path/', get_latest_build_path, name='get_latest_build_path'),
    path('get_project_list/', get_project_list, name='get_project_list'),
    path('execute_commands/', execute_commands, name='execute-commands'),
    path('redirect_dashboard/',redirect_dashboard,name='redirect_dashboard'),

    
]