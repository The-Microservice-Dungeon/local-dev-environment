import os, json
from classes.dev_environment import Dev_Environment
from classes.dungeon_services import Dungeon_Service
import yaml


class Dev_Env_Factory:
    """ Factory class for development environments
    """

    def create_environment(self, version):
        """ Creates new Dev environment object

        Args:
            version (string): Version descriptor for dev environment

        Returns:
            [Dev_Environment]: [description]
        """
        with open(f"config/environments/env_setup_{version}.yml") as f:
            config = yaml.load_all(f, Loader=yaml.FullLoader)
            tmp_env = self.create_environment_object(config)
            print(tmp_env.version)
            tmp_env.save_config()
            tmp_env.setup_environment()
        return tmp_env

    def create_from_available_version(self, environment_version):
        """If a version is aleadry initialized, the object is red from a configuration file

        Args:
            environment_version ([type]): [description]

        Returns:
            [type]: [description]
        """
        if self.check_env_exists(environment_version):
            tmp_env = self.read_env_configs(environment_version)
            tmp_env.setup_networks()
            return tmp_env
        else:
            print(f"No JSON-file for environment:{environment_version}  found! Have you initialized it?")

    def create_environment_object(self, config):
        """Creates the env object

        Args:
            config ([type]): [description]

        Returns:
            [type]: [description]
        """
        service_list = []
        local_version = ""
        for item in config:
            for stuff, attribute in item.items():
                if stuff == 'version':
                    local_version = attribute
                if stuff == 'Services':
                    for key, value in attribute.items():
                        service_list.append(Dungeon_Service(name=key, git_url=value['git_url'], branch=value['branch'],
                                                            filepath=value['filepath']))
            return Dev_Environment(local_version, service_list)

    def read_env_configs(self, environment):
        """reads the env config

        Args:
            environment ([type]): [description]

        Returns:
            [type]: [description]
        """
        with open(f"config/environments/environment_{environment}.json") as jsonFile:
            json_object = json.load(jsonFile)
            jsonFile.close()
        print(json_object)
        services = []
        for service in json_object['services']:
            services.append(Dungeon_Service(service['name'],
                                            service['git_url'],
                                            service['branch'],
                                            service['filepath']))
        tmp_env = Dev_Environment(environment, services)
        return tmp_env

    def check_env_exists(self, version):
        """Checks if env version already exists

        Args:
            version ([type]): [description]

        Returns:
            [type]: [description]
        """
        if os.path.exists(f"config/environments/environment_{version}.json"):

            return True
        else:

            return False
