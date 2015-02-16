import json
from numpy import mean, subtract, square, sqrt
Ucache = json.load(open('/u/mck782/netflix-tests/pma459-usrAvgCache.json', 'r'))
Mcache = json.load(open('/u/mck782/netflix-tests/pma459-mvAvgCache.json', 'r'))
Acache = json.load(open('/u/mck782/netflix-tests/pma459-answersCache.json', 'r'))
#Yearcache = json.load(open('/u/mck782/netflix-tests/es26262-movie-years.json', 'r'))
result = []
answer = []
probe = open('probe.txt', 'r')

currentmid = '1'
result = []
answer = []
probe =  open('probe.txt', 'r')
for line in probe:
    if len(line.split(':')) > 1:
         currentmid = line.split(':')[0]
    else:
         currentuid = line.split('\n')[0]
         r = Acache[currentmid][currentuid]
         pr = ((0.53)*Ucache[currentuid] + (0.4)*Mcache[int(currentmid)]);
         #pr = Mcache[int(currentmid)]
         if (abs(pr - r) > 1):
             print((pr, r))
         result.append(pr)
         answer.append(r)
print(sqrt(mean(square(subtract(result, answer)))))
