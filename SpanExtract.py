import os
import sys
import re
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("textFile", type=str, help="load a text file")
parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("--span", help="set the span of lines to extract", type=int)
parser.add_argument("--duplicates", help="sets the script to print double lines", action="store_true")
parser.add_argument("--mode", help="sets the mode of the script", type=int)
parser.add_argument("--tags", help="sets the tags to search in the text", type=str, nargs='*')
parser.add_argument("--featureTwo", help="sets the second feature to search around the tags", type=str, nargs='*')

args = parser.parse_args()

try:
    path = args.textFile
except IndexError:
    print("Please provide a file name to parse.")
    sys.exit()
try:
    inputFile = open(path)
except IOError:
    print("Please provide a valid .txt-file.")
    sys.exit()

verboseprint = print if args.verbose else lambda *a, **k: None

if args.span:
    span = args.span + 1
else:
    span = 6

if args.duplicates:
    considerduplicates = True
else:
    considerduplicates = False

if args.mode:
    scriptMode = args.mode
else:
    scriptMode = 0

result = open(args.textFile[:-4] + "_Parsed.txt", "w+")
tags = ['((LAUGHS))', '((laughs))', '((laughing))', '((chuckles))', '((chuckling))', '((hehe))', '((heh))', '((ehh))', '((thh))']

if args.tags:
    tags.clear()
    for u in range (0, len(args.tags)):
        tags.append(args.tags[u])
verboseprint("")
verboseprint("Tags to look for: " + str(tags) + "\n""")

lineCount = []

secondFeatures = ['you']

if args.featureTwo:
    secondFeatures.clear()
    for p in range (0, len(args.featureTwo)):
        secondFeatures.append(args.featureTwo[p])
verboseprint("Second Features: " + str(secondFeatures) + "\n""")

tagsFound = 0

featureFound = False


for i, line in enumerate(inputFile):
    for var in tags:
        if re.search(r'\b' + var + '\\b', line):
            if scriptMode == 0:
                verboseprint ("I found " + var + " on line " + str(i))
                tagsFound += 1
                min = i - span
                max = i + span
                for e, line in enumerate(open(path)):
                    while e > min and e < max:
                        if len(lineCount) >= 1:
                            spaceSeeker = int(e) - int(lineCount[-1])
                            if spaceSeeker >= 2:
                                result.write("\n")
                        if considerduplicates and e in lineCount:
                            break
                        lineCount.append(e)
                        result.write(str(e))
                        result.write(" " + line)
                        break
                    if e == max:
                        if considerduplicates == False:
                            result.write("\n")
                        break
            elif scriptMode == 1:
                verboseprint ("I found that line " + str(i) + " contains one or more " + var)
                tagsFound += 1
                min = i - 2
                tag = i
                max = i + 3
                for s, line in enumerate(open(path)):
                    if s == tag or s == tag + 2:
                        for secondFeature in secondFeatures:
                            if re.search(r'\b' + secondFeature + '\\b', line):
                                featureFound = True
                                verboseprint("I found \"" + secondFeature + "\" in the requested lines")
                            else:
                                verboseprint("There is no \"" + secondFeature + "\" in the requested lines")
                        if featureFound == True:
                            for k, line in enumerate(open(path)):
                                while k > min and k < max:
                                    if len(lineCount) >= 1:
                                        spaceSeeker = int(k) - int(lineCount[-1])
                                        if spaceSeeker >= 2:
                                            result.write("\n")
                                    if considerduplicates and i in lineCount:
                                        break
                                    lineCount.append(k)
                                    result.write(str(k))
                                    result.write(" " + line)
                                    break
                                if k == max:
                                    if considerduplicates == False:
                                        result.write("\n")
                                    featureFound = False
                                    verboseprint("")
                                    break
                        else:
                            verboseprint("")
                        break
                    if s == max:
                        featureFound = False
                        verboseprint("")
verboseprint ("I found a total of " + str(tagsFound) + " tags")
result.close()