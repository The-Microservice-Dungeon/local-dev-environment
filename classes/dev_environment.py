import json, os
import tools.helper_tools as tool

from classes import dungeon_services


def setup_default_environment():
    """

    Sets up the default environment with the latest versions of containers etc.

    """
    with open('config/networks.txt') as fp:
        lines = fp.readlines()

    lines = tool.strip_new_lines(lines)

    print("Creating networks:")
    for line in lines:
        line = line.rstrip("\n")
        print(f"Creating {line} network:")
        os.system(f"docker network create {line} || true")


class Dev_Environment:
    """
    class which contains the whole development environment
    """

    def __init__(self, version="", services = []):
        """
        Creates new Dev env object
        Args:
            version (): optional arg. if not set, a default environment is created
        """
        self.services = services
        self.version = version


    def add_service(self, service):
        self.services.append(service)

    def save_config(self):
        jsonStr = json.dumps(self, default=lambda o: o.__dict__, indent=4)
        print(jsonStr)
        f = open(f"config/environments/environment_{self.version}.json", "w+")
        f.write(jsonStr)
        f.close()

    def add_default_services(self):
        # Reads all service names
        with open('config/services.txt') as fp:
            lines = fp.readlines()

        lines = tool.strip_new_lines(lines)
        lines = tool.remove_service_from_list(lines)

        # Adds the Default services
        for line in lines:
            self.services.append(dungeon_services.Dungeon_Service(line, filepath=f"deployment/{line}"))

    def run_environment(self):
        if self.version == "default":
            self.run_default_environment()

    def run_default_environment(self):
        for service in self.services:
            os.system(f'cd {service.filepath} &&  docker-compose -f service-compose.yml up -d  --remove-orphans ')

    def setup_environment(self):
        if self.version == "default":
            print("Setting up default environment: ")
            setup_default_environment()

    def stop_environment(self):

        for service in self.services:
            os.system(f"cd {service.filepath} &&  docker-compose -f service-compose.yml down")

        os.system("docker network prune -f")
