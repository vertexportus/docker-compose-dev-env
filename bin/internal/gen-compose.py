#!/usr/bin/env python3.8

import sys
import traceback
from utils import env, ColoredArgumentParser
from utils.colors import red

command_modules = {
    "docker",
    "shell",
    "git",
}

def gen_compose():
    global verbose
    # config cli commands
    parser = ColoredArgumentParser(prog="gen-compose.py", description='generate the COMPOSE_FILE values based on env config')
    parser.add_argument('-v', '--verbose', action="store_true", help="verbose output")
    # parse args
    args = parser.parse_args()
    verbose = args.verbose
    # generate
    if not env.is_env_projects_set():
        raise Exception("'PROJECTS' env variable must be set")
    services = env.services()
    projects = env.projects()
    output = ''
    compose = ''
    for service, service_name in services.items():
        compose += f"{':' if len(compose) > 0 else ''}docker/compose/{service}.yaml"
        output += f"export {service.upper()}_CONTAINER_NAME='{service_name}'\n"
    for project, project_config in projects.items():
        for service, service_name in project_config['services'].items():
            compose += f"{':' if len(compose) > 0 else ''}docker/compose/{service}.yaml"
            output += f"export {service.upper()}_CONTAINER_NAME='{service_name}'\n"
    output += f"export COMPOSE_FILE={compose}"
    print(output)

verbose = True
if __name__ == '__main__':
    try:
        gen_compose()
    except KeyboardInterrupt:
        print(red("Interrupted"))
        sys.exit(1)
    except Exception as ex:
        if verbose:
            traceback.print_exc()
        else:
            print(red(ex))
        exit(1)
