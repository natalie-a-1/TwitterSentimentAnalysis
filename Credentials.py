import json


class Credentials:

    @staticmethod
    def ReadCredentialInfo(self, file):
        file = open(file)
        jsonFile = json.load(file)
        return jsonFile
