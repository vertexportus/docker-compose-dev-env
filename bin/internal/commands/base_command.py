import os, subprocess, time
import gzip, tarfile, io
import docker
from abc import ABC, abstractmethod
from utils import env

class BaseCommand(ABC):
    @classmethod
    def create_instance(cls, args):
        return cls(args)

    def __init__(self, args):
        self._args = args
    
    @abstractmethod
    def process_command(self):
        pass

    # shell helper methods
    def run_shell(self, command, echo=False):
        if echo:
            print(f"+ {command}")
        subprocess.run(command, shell=True)

    # docker methods
    def container_exec_run(self, container_shortname, command):
        container = self.get_container_by_shortname(container_shortname)
        if container is None:
            raise Exception(f"container '{container_shortname}' not found")
        result = container.exec_run(command, stream=True, demux=False)
        for output in result.output:
            print(output.decode('utf-8'), end='')

    def get_container_by_shortname(self, shortname):
        base_name = f"{env.compose_project_name()}_{shortname}"
        client = docker.from_env()
        containers = client.containers.list()
        for container in containers:
            if shortname in container.name:
                return container
        return None
    def get_container_full_name(self, shortname):
        container = self.get_container_by_shortname(shortname)
        if container is None:
            return None
        else:
            return container.name

    # archive methods
    def gunzip_file(self, file_path):
        with gzip.open(file_path, 'rb') as f:
            file_content = f.read()
        return file_content
    def archive_data(self, data, filename):
        tarstream = io.BytesIO()
        tar = tarfile.TarFile(fileobj=tarstream, mode='w')
        tarinfo = tarfile.TarInfo(name=filename)
        tarinfo.size = len(data)
        tarinfo.mtime = time.time()
        tar.addfile(tarinfo, io.BytesIO(data))
        tar.close()
        tarstream.seek(0)
        return tarstream
