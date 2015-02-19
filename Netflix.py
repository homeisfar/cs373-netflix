import sys
import json
from numpy import mean, subtract, square, sqrt, add, multiply
def netflix_cal():
    Ucache = json.load(open('/u/mck782/netflix-tests/pma459-usrAvgCache.json', 'r'))
    Mcache = json.load(open('/u/mck782/netflix-tests/pma459-mvAvgCache.json', 'r'))
    Acache = json.load(open('/u/mck782/netflix-tests/pma459-answersCache.json', 'r'))

    result = []
    answer = []
#    probe = open('probe.txt', 'r')
    probe = sys.stdin
    currentmid = '1'
    a = []
    b = []

    for line in probe:
        if len(line.split(':')) > 1:
             currentmid = line.split(':')[0]
             print (line, end="")
        else:
             currentuid = line.split('\n')[0]
             r = Acache[currentmid][currentuid]
             val1 = Ucache[currentuid]
             val2 = Mcache[int(currentmid)]
             val3 = val2*0.5 + val1*0.7 - 0.7
             if val3 > 5 :
                 val3 = 5.0
             if val3 < 1 :
                 val3 = 1.0

             print("%.1f" % val3)


             a += (Ucache[currentuid],)
             b += (Mcache[int(currentmid)],)

             answer += (r,)

    mixture = add(multiply(b, 0.5) + multiply(0.7, a), -0.7)
    for i in range(len(mixture)):
        if (mixture[i] > 5):
            mixture[i] = 5
        if (mixture[i] < 1):
            mixture[i] = 1
    print ("RMSE: %.2f" % sqrt(mean(square(subtract(mixture, answer)))))



