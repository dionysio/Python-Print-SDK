import requests as r
import json


class searcher:
    public_key = "7ea493ad22d5930f753cf40e9df9b254bc086a77"
    secret_key = "a8f99f40c29cc677d1740c322720aa3d9243c43a"
    def __init__(self):
        passcode = {"Authorization": "ApiKey {}:{}".format(self.public_key, self.secret_key),
                    "Content-Type": "application/json"}
        self.glob = r.get('https://www.kite.ly/v1.1/template/', headers=passcode).json()
        print(self.glob)

    def name_search(self, criteria):
        for i in range(0, len(self.glob[u'objects'])):
            if criteria == self.glob[u'objects'][i][u'name']:
                return self.glob[u'objects'][i]

    def id_search(self, criteria):
        for i in range(0, len(self.glob[u'objects'])):
            if criteria == self.glob[u'objects'][i][u'template_id']:
                return self.glob[u'objects'][i]

n = searcher()
print('\n')
print(n.name_search('Polaroid minis'))
print('\n')
print(n.id_search(u"polaroids"))
