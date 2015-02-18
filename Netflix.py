import json
from numpy import mean, subtract, square, sqrt, add, multiply
def netflix_cal():
    Ucache = json.load(open('/u/mck782/netflix-tests/pma459-usrAvgCache.json', 'r'))
    Mcache = json.load(open('/u/mck782/netflix-tests/pma459-mvAvgCache.json', 'r'))
    Acache = json.load(open('/u/mck782/netflix-tests/pma459-answersCache.json', 'r'))

    result = []
    answer = []
    probe = open('probe.txt', 'r')

    currentmid = '1'
    result = []
    answer = []
    a = []
    b = []

    for line in probe:
        if len(line.split(':')) > 1:
             currentmid = line.split(':')[0]
        else:
             currentuid = line.split('\n')[0]
             r = Acache[currentmid][currentuid]

             a += (Ucache[currentuid],)
             b += (Mcache[int(currentmid)],)

             answer += (r,)

    mixture = add(multiply(b, 0.5) + multiply(0.7, a), -0.7)
    for i in range(len(mixture)):
        if (mixture[i] > 5):
            mixture[i] = 5
    return (sqrt(mean(square(subtract(mixture, answer)))))



