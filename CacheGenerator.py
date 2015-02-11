#CacheGenerator.py
import json
import sys
import os

# infile = open('/home/alih/school/cs373-SWE/netflix/netflix/training_set/mv_0002734.txt', 'r')


ratinglist = []
moviedict = {}
for root, dirs, files in os.walk('/home/alih/school/cs373-SWE/netflix/netflix/training_set/'):
	for filename in files:
	
		infile = open(root + filename, 'r')

		movie = int(infile.readline().split(":")[0])

		for line in infile:
			splitline = line.split(",")
			ratinglist.append (int(splitline[1]))

		moviedict[movie] = ratinglist

#for line in infile:
#	print (line, end="")


#with open('output', 'w') as outfile:
#	json.dump(mv_0002734, outfile)