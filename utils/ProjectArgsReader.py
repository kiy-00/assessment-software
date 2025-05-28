import json
import os


class ProjectArgsReader:
    def __init__(self, folder):
        self.folder = folder
        self.data = json.load(open(os.path.join(folder, 'User_input.json')))
