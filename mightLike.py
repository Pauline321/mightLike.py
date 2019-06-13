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

for songNum in range(len(sList)):
    if sList[songNum][maxVV + 10] == maxVal:
        print("---*---")
        mvMatches.append(sList[songNum])

print("There are", len(mvMatches), "matches for that maximum rating.")
print(mvMatches[0]) 

##if dinstMatches == 1:
##    print("You may also like", dinstMatch[0][0], "by", dinstMatch[0][1])
