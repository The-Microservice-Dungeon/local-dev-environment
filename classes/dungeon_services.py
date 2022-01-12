import os, json


class Dungeon_Service:

    def __init__(self, name, git_url = "",branch = "master", filepath = ""):
        self.name = name
        self.git_url = git_url
        self.branch = branch
        self.filepath = filepath
