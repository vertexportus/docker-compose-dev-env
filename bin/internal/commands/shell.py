from . import base_command

class Shell(base_command.BaseCommand):
    @staticmethod
    def argparse(parser, subparsers):
        parser_main = subparsers.add_parser('shell', help="runs a shell inside a specified container")
        parser_main.add_argument('container', help="container to run shell in")

    def process_command(self):
        self.run_shell(f"docker-compose exec {self._args.container} sh -c \"which bash > /dev/null 2>&1 && bash || sh\"")