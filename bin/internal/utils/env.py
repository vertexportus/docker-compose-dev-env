import os

def with_default(varname, default):
    return os.environ[varname] if varname in os.environ else default

def cli_command():
    return os.environ['CLI_COMMAND']

def compose_project_name():
    return with_default('COMPOSE_PROJECT_NAME', 'compose')
