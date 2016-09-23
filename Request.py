

from cassiopeia import riotapi
from cassiopeia.type.core.common import EventType
from cassiopeia.type.dto import *

class module:

    def __init__(self, name, region):
        self.name = name
        self.region = region

    def setregion(self):

        region = riotapi.set_region(self.region)

    def getsummoner(self):

        summoner = riotapi.get_summoner_by_name(self.name)
        return summoner

    def getrecentmatch(self):

        match_list = riotapi.get_match_list(self.getsummoner(), num_matches=5)
        match = match_list[0].match()

        return match










