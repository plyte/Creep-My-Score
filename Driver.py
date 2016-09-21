# Name: Driver.py
# Author: Matthew Jones
# Purpose: To house the Main function and any other initializations made
# Date: 08/25/16

import sOE
import Request
import requests
import json
import string

def main():

    nameimput = 'céll'
    summoner = Request.Request(name=nameimput)
    matchlist = Request.Request.callmatchlist(summoner.callid, 2015)
    print(summoner.callid)
    print(matchlist)


if __name__ == "__main__":
    main()


