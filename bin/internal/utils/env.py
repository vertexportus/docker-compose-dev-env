import os, re

def with_default(varname, default):
    return os.environ[varname] if varname in os.environ else default
def try_get(varname):
    if varname in os.environ:
        return os.environ[varname]
    else:
        raise Exception(f"'{varname}' not set in env")

def cli_command():
    return os.environ['CLI_COMMAND']
def git_use_https():
    return with_default('GIT_USE_HTTPS', '0') == '1'

def compose_project_name():
    return with_default('COMPOSE_PROJECT_NAME', 'compose')
def services(override=None):
    services = {}
    raw_services = override.split(',') if override else with_default('SERVICES', '').split(',')
    for raw_service in raw_services:
        if ':' in raw_service:
            raw_service_split = raw_service.split(':')
            services[raw_service_split[0]] = raw_service_split[1]
        else:
            services[raw_service] = raw_service
    return services

def is_env_projects_set():
    return 'PROJECTS' in os.environ
def projects():
    projects = {}
    project_names = map(lambda p: p.strip(), os.environ['PROJECTS'].split(','))
    for raw_project_name in list(project_names):
        project_var_name = re.sub('(?!^)([A-Z]+)', r'_\1', raw_project_name).upper()
        var_folder = f"PROJECT_{project_var_name}_FOLDER"
        var_git = f"PROJECT_{project_var_name}_GIT"
        var_services = f"PROJECT_{project_var_name}_SERVICES"
        project_name = raw_project_name.upper()
        projects[raw_project_name] = {
            "repo_url": try_get(var_git),
            "folder" : os.environ[var_folder] if var_folder in os.environ else f"src/{project_var_name.lower()}",
            "services" : services(os.environ[var_services]) if var_services in os.environ else {}
        }
    return projects

    # p = {}
    # regex = re.compile('PROJECT_(\w+)')
    # for k, v in os.environ.items():
    #     if k.startswith('PROJECT_'):
    #         project_name = regex.match(k).group(1).lower()
    #         p[project_name] = v
    # return p
