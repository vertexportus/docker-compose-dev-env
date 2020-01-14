import os, re

def with_default(varname, default):
    return os.environ[varname] if varname in os.environ else default

def cli_command():
    return os.environ['CLI_COMMAND']
def git_use_https():
    return with_default('GIT_USE_HTTPS', '0') == '1'

def compose_project_name():
    return with_default('COMPOSE_PROJECT_NAME', 'compose')

def projects():
    p = {}
    regex = re.compile('PROJECT_(\w+)')
    for k, v in os.environ.items():
        if k.startswith('PROJECT_'):
            project_name = regex.match(k).group(1).lower()
            p[project_name] = v
    return p
