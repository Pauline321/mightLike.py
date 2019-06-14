#might.like.py by Pauline Akhi Eloge and Josh

import csv

#initialize variables

uTitle = "No guidance"
uCre = "chris brown"
uPerf = "chris brown, drake"
uLang = "english" 
uRec =  2019
uGen = "hip-hop"
uSgen = "rap"
uTop =  "sad"
uMood = "upbeat"
uDinst = "synthesizer"
uInsk = 7 # maxVar 0
uLyr =  8 # maxVar 1
uVoc = 8  # maxVar 2
uMel = 9  # maxVar 3
uRhy = 8  # maxVar 4
uDdr = 8  # maxVar 5
Tpo = 7   # maxVar 6

subjInt = (uInsk, uLyr, uVoc, uMel, uRhy, uDdr, Tpo) # Tuple of subjective integers

sList = [] # This list will hold all the songs from our library.
mvMatches = [] # This list will hold max value matches.
genMatches = [] # This list will hold genre matches.
topMatches = [] # This list will hold topic matches
sList = [row for row in csv.reader(open("sLibS19.tsv", encoding='utf-8'), delimiter="\t")] # Load song library.

del sList[0] # Delete column titles from song lib.
del sList[0] # Delete columns data types frpm song lib.

for songNum in range(len(sList)):
    sList[songNum][4] = int(sList[songNum][4]) # Transform rec date from string to integer.

for songNum in range(len(sList)): # Transform subj ints from strings to integers.
    for elemNum in range(7):
        sList[songNum][elemNum + 10] = int(sList[songNum][elemNum + 10])

##for song in range(5):
##    print (sList[song])

maxVal = max(subjInt) # Find max of subj. int.s.
print(maxVal)
maxVars = [i for i, j in enumerate(subjInt) if j == maxVal] # Find positions in tuple of subj. int.s.
print(maxVars)  # songVar index = maxVar + 10
maxVV = maxVars[0]
print(maxVV + 10)

#------max value matches Search 1 ------
for songNum in range(len(sList)):
    if sList[songNum][maxVV + 10] == maxVal:
        #print("---*---")
        mvMatches.append(sList[songNum])

print("There are", len(mvMatches), "matches for that maximum rating.")
#print(mvMatches[0])

search2 = []

if len(mvMatches) == 1:
    print("You may also like", mvMatches[0][0], "by", mvMatches[0][1], ".")
    exit()
elif len(mvMatches) > 1:
    search2 = mvMatches
else:
    search2 = sList
print(len(search2))
#-------genre matches Search 2 ---------
for songNum in range(len(search2)):
    if search2[songNum][5] == uGen:
        genMatches.append(search2[songNum])

print("There are", len(genMatches), "matches for that genre.")
print(genMatches[0])

search3 = []

if len(genMatches) == 1:
    print("You may also like", genMatches[0][0], "by", genMatches[0][1], ".")
    exit()
elif len(genMatches) > 1:
    search3 = genMatches
else:
    if len(mvMatches) == 0:
        search3 = sList
    else:
        search3 = mvMatches
print(len(search3))



#------topic matches---------
for songNum in range (len(genMatches)):
    if genMatches[songNum][8] == uTop:
        topMatches.append(genMatches[songNum])

print("There are", len(topMatches), "matches for that topic.")
print( topMatches[0])

search4 = []

if len(topMatches) == 1:
    print("You may also like", topMatches[0][0], "by", topMatches[0][1], ".") 
    exit()
elif len(topMatches) > 1:
    search4 = topMatches
else:
    search4 = sList
print(len(search4))

print(search4)

        






