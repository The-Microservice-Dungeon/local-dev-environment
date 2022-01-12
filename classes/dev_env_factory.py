import os, json
from classes.dev_environment import Dev_Environment
from classes.dungeon_services import Dungeon_Service


class Dev_Env_Factory:

    def create_environment(self):
        self.create_default_environment()

    def create_default_environment(self):
        if self.check_env_exists("default"):
            return self.read_env_configs("default")


    def read_env_configs(self, environment):
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
        if os.path.exists(f"config/environments/environment_{version}.json"):
            print(("True"))
            return True
        else:
            print(("False"))
            return False
