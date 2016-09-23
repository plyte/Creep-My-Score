import os, sOE
import matplotlib.pyplot as plt

from Request import module
from cassiopeia import riotapi
from cassiopeia.type.core.common import LoadPolicy
import pprint


def main():
    name = "Céll"
    region = "NA"
    key = os.environ["DEV_KEY"]
    riotapi.set_api_key(key)
    riotapi.set_load_policy(LoadPolicy.lazy)
    riotapi.set_region(region=region)
    riotapi.print_calls(True)

    m = module(name=name, region=region)
    summoner = m.getsummoner()
    match = m.getrecentmatch()

    creep_score_timeline = {}
    minute_val = {}

    for frame in match.timeline.frames:
        for participant, participant_frame in frame.participant_frames.items():
            if summoner.id == participant.summoner_id:
                creep_score_timeline[int(frame.timestamp.seconds / 60)] = (participant_frame.minion_kills +
                                                                           participant_frame.jungle_monsters_killed)

    pp = pprint.PrettyPrinter()
    print(creep_score_timeline)

    width = 1.0
    plt.bar(creep_score_timeline.keys(), creep_score_timeline.values(), width, color='g')

    plt.show()

    #for data_dict in creep_score_timeline.iteritems():
    #    x = data_dict.keys()
    #    y = data_dict.values()
    #    plt.figure()
    #    plt.plot(x,y)

    #plt.legend(creep_score_timeline.keys())
    #plt.show()

if __name__ == "__main__":
    main()
