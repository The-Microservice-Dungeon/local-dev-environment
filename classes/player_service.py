import os
import json


class Player_Service:

    def __init__(self, config=""):

        self.running = False

        if config == "":
            self.write_config()
            self.initialized = True
            jsonStr = json.dumps(self.__dict__)

            f = open("classes/player_configs/config.json", "w+")

            f.write(jsonStr)
            f.close()

        else:
            f = open(config)
            service_dict = json.load(f)
            print(service_dict)
            self.initialized = service_dict["initialized"]
            self.filepath = service_dict["filepath"]

            print(f"PlayerObject loaded {self.filepath}")

    def write_config(self):

        filepath = input(
            "Please add the location of your player-service on your machine\n")

        self.filepath = filepath

        print(f"Your filepath {filepath} has been added")
    
    def run_player(self):
        os.system(f"cd {self.filepath} && docker-compose up")
