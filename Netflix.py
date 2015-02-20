import sys
import json
from numpy import mean, subtract, square, sqrt, add, multiply
def netflix_cal(r, w):
    Ucache = json.load(open('/u/mck782/netflix-tests/pma459-usrAvgCache.json', 'r'))
    Mcache = json.load(open('/u/mck782/netflix-tests/pma459-mvAvgCache.json', 'r'))
    Acache = json.load(open('/u/mck782/netflix-tests/pma459-answersCache.json', 'r'))
    Ycache = json.load(open('/u/mck782/netflix-tests/af22574-movieDates.json', 'r'))
    MYcache = json.load(open('/u/mck782/netflix-tests/cdm2697-userRatingsAveragedOver10yInterval-v2.json', 'r'))
    result = []
    answer = []
    probe = sys.stdin
    currentmid = '1'
    a = []
    b = []

    for line in probe:
        f = 0
        if len(line.split(':')) > 1:
             currentmid = line.split(':')[0]
             w.write (line)
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
             f = []
             if (currentmid in Ycache and not Ycache[currentmid] == 'NULL'):
                 if (currentuid in MYcache):
                     year = int(Ycache[currentmid])
                     year = (year // 10) * 10
                     for l in MYcache[currentuid]:
                         if l[0] == year: 
                             f += (val3 * 0.5 + 0.5*l[1],)
  
             if (f == []):
                 result += (val3,)
             else:
                 result += (f[0],)
             w.write("%.1f\n" % val3)

             answer += (r,)

    for i in range(len(result)):
        if (result[i] > 5):
            result[i] = 5
        if (result[i] < 1):
            result[i] = 1
    w.write ("RMSE: ")
    w.write (str(int(100*sqrt(mean(square(subtract(result, answer)))))/100.0))
    w.write ("\n")


# TODO: Finish unit tests
# TODO: Finish pre-post asserts
# TODO: Create log
# TODO: Create pydoc
# TODO: Create SHA (last)

# TODO: Ali Homafar ah26482 home.isfar@gmail.com
