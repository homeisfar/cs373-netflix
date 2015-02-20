#!/usr/bin/env python3
import sys
import json
# An earlier version of the code imported numpy, but we removed
# all numpy imports to not mess with coverage3 being incapable
# of finding numpy.

def netflix_load_cache():
    f = open('/u/mck782/netflix-tests/pma459-usrAvgCache.json', 'r')
    Ucache = json.load(f)
    f.close()
    
    f = open('/u/mck782/netflix-tests/pma459-mvAvgCache.json', 'r')
    Mcache = json.load(f)
    f.close()

    f = open('/u/mck782/netflix-tests/pma459-answersCache.json', 'r')
    Acache = json.load(f)
    f.close()

    f = open('/u/mck782/netflix-tests/af22574-movieDates.json', 'r')
    Ycache = json.load(f)
    f.close()

    f = open('/u/mck782/netflix-tests/cdm2697-userRatingsAveragedOver10yInterval-v2.json', 'r')
    MYcache = json.load(f)
    f.close()
    return (Ucache, Mcache, Acache, Ycache, MYcache)

def netflix_read(s):
    # Every movie ID ends with a colon. Every other line is just a number
    assert type(s) is str
    if len(s.split(':')) > 1:
        currentmid = s.split(':')[0]
        return (True, currentmid)
    else :
        currentuid = s.split('\n')[0]
        return (False, currentuid)


def netflix_cal(currentmid, currentuid, cache):
    assert int(currentmid) > 0
    assert int(currentmid) < 17771
    assert int(currentuid) > 0
    assert int(currentuid) < 2649430
    Ucache, Mcache, Acache, Ycache, MYcache = cache
    val1 = Ucache[currentuid]
    val2 = Mcache[int(currentmid)]
    val3 = val2*0.5 + val1*0.7 - 0.7

    # Our calculations can produce values above and below 1 & 5.
    # Since ratings are 1-5 inclusive, we ceil/floor the values
    if val3 > 5 :
        val3 = 5.0
    if val3 < 1 :
        val3 = 1.0

    assert val3 <= 5.0 and val3 >= 1.0

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
    val3 = int(val3 * 10) / 10.0

    return (val3, Acache[currentmid][currentuid])

# Pass in IOStreams on read and write for STDIN and STDOUT
# This code has to be run from RunNetflix.py
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
            w.write(str(pred) + '\n')
            p += (pred,)
            a += (actual,)
    result = list(zip(p,a))
    length = len(result)
    v = sum([(x - y) ** 2 for x, y in result])/length
    rmse = v ** (1/2)

    assert type(rmse) is float
    w.write('RMSE: ' + str(int(rmse * 100.0)/100.0) + '\n')

