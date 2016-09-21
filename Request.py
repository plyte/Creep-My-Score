# Name: Request.py
# Purpose: To call the riot API
# Date: 08/25/16
# Author: Matthew Jones

import requests
import Consts
import json
import sOE


def callid(name):
    key = Consts.URL['key']
    region = Consts.REGION['North_America']
    version = Consts.VERSION['version']
    url = Consts.URL['summoner'].format(
        region=region,
        key=key,
        version=version,
        ame=name
    )
    apiobjectci = requests.get(url)
    jsondata = dict(json.loads(apiobjectci.text))
    sumid = jsondata[name]['id']

    return sumid


def callmatchlist(sumid,year):
    key = Consts.URL['key']
    region = Consts.REGION['North_America']
    url = Consts.URL['matchlist'].format(
        region=region,
        key=key,
        sumid=sumid,
        typeOfRanked=Consts.URL['RANKED_SOLO_5x5'],
        year=year
    )
    apiobjectml = requests.get(url)
    matchlist = dict(json.loads(apiobjectml.text))

    return matchlist


def specificmatchinfo(matchid):
    key = Consts.URL['key']
    region = Consts.REGION['North_America']
    url = Consts.URL['match'].format(
        region=region,
        key=key,
        matchid=matchid,
    )
    apiobjectm = requests.get(url)
    match = dict(json.loads(apiobjectm.text))

    return match