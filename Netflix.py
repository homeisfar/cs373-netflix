#!/usr/bin/env python3
import sys
import json
from numpy import mean, subtract, square, sqrt, add, multiply

def netflix_load_cache():
    Ucache = json.load(open('/u/mck782/netflix-tests/pma459-usrAvgCache.json', 'r'))
    Mcache = json.load(open('/u/mck782/netflix-tests/pma459-mvAvgCache.json', 'r'))
    Acache = json.load(open('/u/mck782/netflix-tests/pma459-answersCache.json', 'r'))
    Ycache = json.load(open('/u/mck782/netflix-tests/af22574-movieDates.json', 'r'))
    MYcache = json.load(open('/u/mck782/netflix-tests/cdm2697-userRatingsAveragedOver10yInterval-v2.json', 'r'))
    return (Ucache, Mcache, Acache, Ycache, MYcache)

def netflix_read(s):
    if len(s.split(':')) > 1:
        currentmid = s.split(':')[0]
        return (True, currentmid)
    else :
        currentuid = s.split('\n')[0]
        return (False, currentuid)


def netflix_cal(currentmid, currentuid, cache):
    Ucache, Mcache, Acache, Ycache, MYcache = cache
    val1 = Ucache[currentuid]
    val2 = Mcache[int(currentmid)]
    val3 = val2*0.5 + val1*0.7 - 0.7
    if val3 > 5 :
        val3 = 5.0
    if val3 < 1 :
        val3 = 1.0

    if (currentmid in Ycache and not Ycache[currentmid] == 'NULL'):
        if (currentuid in MYcache):
            year = int(Ycache[currentmid])
            year = (year // 10) * 10
            for l in MYcache[currentuid]:
                if l[0] == year: 
                    val3 = val3 * 0.5 + 0.5*l[1]
                    break
    
    if val3 > 5:
        val3 = 5.0
    if val3 < 1:
        val3 = 1.0
    return (val3, Acache[currentmid][currentuid])


def netflix_solve(r, w) :
    """
    r a reader
    w a writer
    """
    cache = netflix_load_cache()
    mid = '1'
    uid = '1'
    p = []
    a = []
    for s in r:
        if_this_is_mid, data = netflix_read(s)
        if if_this_is_mid:
            mid = data
            w.write(mid + ':\n')
        else:
            uid = data
            pred, actual = netflix_cal(mid, uid, cache)
            w.write(str(int(pred * 10) / 10.0) + '\n')
            p += (pred,)
            a += (actual,)
    rmse = sqrt(mean(square(subtract(p, a))))
    w.write('RMSE: ' + str(int(rmse * 100.0)/100.0))


# TODO: Finish unit tests
# TODO: Finish pre-post asserts
# TODO: Create log
# TODO: Create pydoc
# TODO: Create SHA (last)

# TODO: Ali Homafar ah26482 home.isfar@gmail.com

