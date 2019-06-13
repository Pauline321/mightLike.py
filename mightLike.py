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
utop =  "love"
uMood = "upbeat"
uDinst = "synthesizer"
uInsk = 7
uLyr =  8
uVoc = 8
uMel = 9
uRhy = 9
uDdr = 8
Tpo = 7

subjInt = (uInsk, uLyr, uVoc, uMel, uRhy, uDdr, Tpo)

sList = [] # This list will hold all the songs from our library.
dinstMatches = [] # This list will hold dinst matches.

sList = [row for row in csv.reader(open("sLibS19.tsv", encoding='utf-8'), delimiter="\t")]

del sList[0]
del sList[0]

for song in range(len(sList)):
    sList[song][4] = int(sList[song][4])

##for song in range(5):
##    print (sList[song])

maxVal = max(subjInt)
print(maxVal)
maxVars = [i for i, j in enumerate(subjInt) if j == maxVal]
print(maxVars)

for songNum in range(len(sList)):
    if uDinst == sList[songNum][9]:
        dinstMatches.append(sList[songNum])

print("There are", len(dinstMatches), "matches for dominant instruments.")

if dinstMatches == 1:
    print("You may also like", dinstMatch[0][0], "by", dinstMatch[0][1])
