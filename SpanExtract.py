question = raw_input("How would you like to name your output file?")

if question != "":
    # Create and name output file
    fileName = question + ".txt"
    result = open(fileName,"w+")
else:
    result = open("Parsed.txt", "w+")

import os
import sys

# read command line argument
try:
    path = sys.argv[1]
except IndexError:
    print("Please provide a file name to parse.")
    sys.exit()

# read file
try:
    search = open(path)
except IOError:
    print("Please provide a valid .txt-file.")
    sys.exit()

# If a third argument is identified, that becomes the span
if len(sys.argv) >= 3:
    span = int(sys.argv[2]) + 1
else:
    span = 6

# If a fourth argument is identified, that sets the script from not printing out double lines, to printing out double lines
if len(sys.argv) >= 4:
    mode = int(sys.argv[3])

tags = []
defaultTags = ['((LAUGHS))', '((laughs))', '((laughing))', '((chuckles))', '((chuckling))', '((hehe))', '((heh))', '((ehh))', '((thh))']
userTags = []

# Switches markers from default to user set
if len(sys.argv) >= 5:
    for u in range (4, len(sys.argv)):
        userTags.append(sys.argv[u])
    tags = userTags
else:
    tags = defaultTags

print tags

lineCount = []

print len(tags)

for i, line in enumerate(search):
    for c in range (0, len(tags)):
        var = tags[c]
        if var in line:
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
                                break
                    elif mode == 1:
                        while i > min and i < max:
                            result.write(str(i))
                            result.write(" " + line)
                            break
                        if i == max:
                            result.write("\n")
result.close()