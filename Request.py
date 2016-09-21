# Name: Request.py
# Purpose: To call the riot API
# Date: 08/25/16
# Author: Matthew Jones

import requests
import Consts
import json


class Request:

    # initialize the variables
    def __init__(self, name):
        self.name=name

    # utilize the requests module to call the api

    @property
    def callid(self):
        key = Consts.URL['key']
        region = Consts.REGION['North_America']
        version = Consts.VERSION['version']
        url = Consts.URL['summoner'].format(
            region=region,
            key=key,
            version=version,
            name=self.name
        )
        apiobjectci = requests.get(url)
        jsondata = dict(json.loads(apiobjectci.text))

        sumid = jsondata[self.name]['id']

        return sumid

    def callmatchlist(sumID,year):
        key = Consts.URL['key']
        region = Consts.REGION['North_America']
        url = Consts.URL['matchlist'].format(
            region=region,
            key=key,
            sumID=sumID,
            typeOfRanked=Consts.URL['RANKED_SOLO_5x5'],
            year=year
        )
        apiobjectml = requests.get(url)
        matchlist = dict(json.loads(apiobjectml.text))

        return matchlist