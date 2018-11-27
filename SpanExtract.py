# Naming the parsed output file
question = raw_input("How would you like to name your output file?\n")

if question != "":
    # Create and name output file
    fileName = question + ".txt"
    result = open(fileName,"w+")
else:
    result = open("Parsed.txt", "w+")

import os
import sys

# Read command line argument input file
try:
    path = sys.argv[1]
except IndexError:
    print("Please provide a file name to parse.")
    sys.exit()

# Open file provided in first argument
try:
    search = open(path)
except IOError:
    print("Please provide a valid .txt-file.")
    sys.exit()

# If a second argument is identified, that becomes the span
if len(sys.argv) >= 3:
    span = int(sys.argv[2]) + 1
else:
    span = 6

# If a third argument is identified, that sets the script from not printing out double lines, to printing out double lines
if len(sys.argv) >= 4:
    mode = int(sys.argv[3])

# If a fourth argument is identified, that sents the script from printing only markers that contain a certain word in the span
if len(sys.argv) >= 5:
    truffleDog = int(sys.argv[4])

tags = []
defaultTags = ['((LAUGHS))', '((laughs))', '((laughing))', '((chuckles))', '((chuckling))', '((hehe))', '((heh))', '((ehh))', '((thh))']
userTags = []

# Switches markers from default to user set
if len(sys.argv) >= 6:
    for u in range (5, len(sys.argv)):
        userTags.append(sys.argv[u])
    tags = userTags
else:
    tags = defaultTags

print tags

lineCount = []

truffle = 'you'

we = 0

truffleFound = False

for i, line in enumerate(search):
    for c in range (0, len(tags)):
        var = tags[c]
        if var in line:
            if truffleDog == 0:
                print ("I found " + var + " on line " + str(i))
                min = i - span
                max = i + span
                for i, line in enumerate(open(path)):
                        if mode == 0:
                            while i > min and i < max:
                                if i in lineCount:
                                    break
                                else:
                                    lineCount.append(i)
                                    result.write(str(i))
                                    result.write(" " + line)
                        elif mode == 1:
                            while i > min and i < max:
                                result.write(str(i))
                                result.write(" " + line)
                                break
                            if i == max:
                                result.write("\n")
            elif truffleDog == 1:
                print ("I found that line " + str(i) + " contains one or more " + var)
                we = we + 1
                # print str(we)
                # print ("Sniffing for truffles on line " + str(i))
                min = i - 2
                tag = i
                max = i + 3
                for i, line in enumerate(open(path)):
                    while i > min and i < max:
                        if truffle in line:
                            if i == tag:
                                truffleFound = True
                            elif i == tag + 2:
                                truffleFound = True
                        if truffleFound == True:
                            for c, line in enumerate(open(path)):
                                while c > min and c < max:
                                    result.write(str(c))
                                    result.write(" " + line)
                                    break
                                if c == max:
                                    result.write("\n")
                                    truffleFound = False
                        else:
                            if i == tag:
                                print "There is no \"" + truffle + "\" in line " + str(i)
                            elif i == tag + 2:
                                print "There is no \"" + truffle + "\" in line " + str(i)
                        break
                    if i == max:
                        truffleFound = False
                        print ""
result.close()