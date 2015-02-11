#CacheGenerator.py
import json
import sys
import os

from collections import Counter

movieList = open('/home/alih/school/cs373-SWE/netflix/netflix/movie_titles.txt', 'r')
movieDict = {}

for line in movieList :
	splitLine = line.split(",")
	#print (splitLine)
	movieDict[splitLine[0]] = [splitLine[1]]


x = 0

for root, dirs, files in os.walk('/home/alih/school/cs373-SWE/netflix/netflix/training_set/') :

	# Go through every file in the training set
	for filename in files:

		if x == 3 :
			break
		
		# infoList represents multiple bits of data. [0] is the average, [1] is the mode, [2]
		#infoList = []
		# list of every rating a movie has received
		ratingList = []
	
		infile = open(root + filename, 'r')
		# The first line (Movie ID) has the colon removed and is converted to an int
		movie = int(infile.readline().split(":")[0])

		#Store every rating in the list
		for line in infile:
			splitline = line.split(",")
			ratingList.append (int(splitline[1]))

		average = sum(ratingList) / len(ratingList)

		average = round(average,3)


		mode = Counter(ratingList)

		movieDict[movie].append(average)
		movieDict[movie].append(mode.most_common(1)[0])
#		infoList.append(ratingList)

#		movieDict[movie] = infoList

		x += 1

with open ('output', 'w') as outfile:
	json.dump (movieDict, outfile)

testinfile = open('output', 'r')
moviedict2 = json.loads(testinfile.read())
print (moviedict2)
print ("Done")