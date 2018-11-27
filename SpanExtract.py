# Naming the parsed output file
question = input("How would you like to name your output file?\n")

if question != "":
    # Create and name output file
    fileName = question + ".txt"
    result = open(fileName,"w+")
else:
    result = open("Parsed.txt", "w+")

import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("textFile", type=str, help="load a text file")
parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("--span", help="set the span of lines to extract", type=int)
parser.add_argument("--duplicates", help="sets the script to print double lines", action="store_true")
parser.add_argument("--mode", help="sets the mode of the script", type=int)

args = parser.parse_args()

verbose = False
try:
    path = args.textFile
except IndexError:
    print("Please provide a file name to parse.")
    sys.exit()
try:
    search = open(path)
except IOError:
    print("Please provide a valid .txt-file.")
    sys.exit()

if args.verbose:
    verbose = True
    def verboseprint(*args):
        # Print each argument separately so caller doesn't need to
        # stuff everything to be printed into a single string
        for arg in args:
           print (arg),
        print
else:   
    verboseprint = lambda *a: None

if args.span:
    span = args.span
else:
    span = 6

if args.duplicates:
    mode = args.duplicates
else:
    mode = 0

if args.mode:
    truffleDog = args.mode
else:
    truffleDog = 0



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

verboseprint(tags)

lineCount = []

truffle = 'you'

we = 0

truffleFound = False

for i, line in enumerate(search):
    for c in range (0, len(tags)):
        var = tags[c]
        if var in line:
            if truffleDog == 0:
                verboseprint ("I found " + var + " on line " + str(i))
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
                verboseprint ("I found that line " + str(i) + " contains one or more " + var)
                we = we + 1
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
                                verboseprint("There is no \"" + truffle + "\" in line " + str(i))
                            elif i == tag + 2:
                                verboseprint("There is no \"" + truffle + "\" in line " + str(i))
                        break
                    if i == max:
                        truffleFound = False
                        verboseprint("")
result.close()