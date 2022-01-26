import json, os, time
import classes.tools.helper_tools as tool


class Dev_Environment:
    """
    class which contains the whole development environment
    """

    def __init__(self, version="", services=[]):
        """
        Creates new Dev env object
        Args:
            version (): optional arg. if not set, a default environment is created
        """
        self.services = services
        self.version = version

    def setup_networks(self):
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

    def save_config(self):
        """Saves config to JSON file
        """
        jsonStr = json.dumps(self, default=lambda o: o.__dict__, indent=4)
        print(jsonStr)
        f = open(f"config/environments/environment_{self.version}.json", "w+")
        f.write(jsonStr)
        f.close()

    def run_environment(self):
        """Runs the environment


        """
        for service in self.services:
            if service.name == "kafka":
                os.system(f'cd {service.filepath} &&  docker-compose -f service-compose.yml up -d  --remove-orphans ')
        
        print("Giving Kafka some time to start... be patient :-)")
        time.sleep(60)

        for service in self.services:
            if service.name != "kafka":
                os.system(f'cd {service.filepath} &&  docker-compose -f service-compose.yml up -d  --remove-orphans ')

    def setup_environment(self):
        """ Environment setup
        """
        if self.version == "default":
            print("Setting up default environment: ")
            self.setup_networks()
        else:
            self.setup_custom_environment()
            self.setup_networks()

    def update_all_containers(self):
        """Updates all images
        """
        self.stop_environment()
        for service in self.services:
            os.system(f"cd {service.filepath} &&  docker-compose -f service-compose.yml pull")

    def delete_containers_networks(self):
        """deletes networks and containers
        """
        self.stop_environment()

        with open('config/images.txt') as fp:
            lines = fp.readlines()
            lines = tool.strip_new_lines(lines)
            for line in lines:
                os.system(f"docker rmi {line}")

    def setup_custom_environment(self):
        """Sets up custom env
        """
        os.system("mkdir custom_environments")
        os.system(f"mkdir custom_environments/version_{self.version}")
        for service in self.services:
            print(service.git_url)
            os.system(f"cd custom_environments/version_{self.version} && git clone {service.git_url} ")
            service.filepath = f"custom_environments/version_{self.version}/{service.name}"
        self.save_config()

    def stop_environment(self):
        """stops the environment
        """

        for service in self.services:
            os.system(f"cd {service.filepath} &&  docker-compose -f service-compose.yml down")

        os.system("docker network prune -f")
