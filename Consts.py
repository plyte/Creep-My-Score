import os
import sOE

URL = {


    'key': os.environ["RIOT_API_KEY"],
    'RANKED_SOLO_5x5': 'RANKED_SOLO_5x5',

    'summoner': 'https://{region}.api.pvp.net/api/lol/{region}/v{version}/summoner/by-name/{name}?api_key={key}',
    'matchlist': 'https://{region}.api.pvp.net/api/lol/{region}/v2.2/matchlist/by-summoner/{sumid}'
                 '?rankedQueues={typeOfRanked}&seasons=SEASON{year}&api_key={key}',
    'match': 'https://{region}.api.pvp.net/api/lol/{region}/v2.2/match/{matchid}?includeTimeline=True&api_key={key}'

}

REGION = {

    'North_America': 'na',

}

VERSION = {

    'version': '1.4',

}