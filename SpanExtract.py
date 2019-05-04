import os
import sys
import re
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--fileParsing", type=str, help="load a single text file")
parser.add_argument("--folderParsing", type=str, help="iterate through a folder of text files")
parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("--span", help="set the span of lines to extract", type=int)
parser.add_argument("--duplicates", help="sets the script to print double lines", action="store_true")
parser.add_argument("--mode", help="sets the mode of the script", type=int)
parser.add_argument("--tags", help="sets the tags to search in the text", type=str, nargs='*')
parser.add_argument("--featureTwo", help="sets the second feature to search around the tags", type=str, nargs='*')
parser.add_argument("--subMode", help="sets the submode of mode 1", type=int)
parser.add_argument("--output", help="sets the type of output, txt or xls", type=str)

args = parser.parse_args()

hits = 0
secondFeatures = ['you']
openFile = []
fileOutput = 'txt'
lineCount = []
spaceSeeker = 0
printedSpans = 0
ignoredTags = 0
# Unused Variables
# tagsFound = 0
# featureFound = False


verboseprint = print if args.verbose else lambda *a, **k: None

if args.fileParsing:
    try:
        openfile = args.fileParsing
    except IndexError:
        print("Please provide a file name to parse.")
        sys.exit()

if args.folderParsing:
    folder = args.folderParsing
    verboseprint('Folder being parsed = ' + folder)
    print('Absolute path of the folder being parsed = ' + os.path.abspath(folder))
    for root, subdirs, files in os.walk(folder):
        for filename in files:
            if filename != '.DS_Store':
                file_path = os.path.join(root, filename)
                openFile.append(file_path)

if args.span:
    span = args.span
else:
    span = 5

if args.duplicates:
    considerduplicates = True
else:
    considerduplicates = False

if args.mode:
    scriptMode = args.mode
else:
    scriptMode = 0

tags = ['((laughs))', '((laughing))', '((chuckles))', '((chuckling))', '((hehe))', '((heh))', '((ehh))', '((thh))']

if args.tags:
    tags.clear()
    for u in range (0, len(args.tags)):
        tags.append(args.tags[u])
    verboseprint("")
    verboseprint("Tags to look for: " + str(tags) + "\n""")

if args.featureTwo:
    secondFeatures.clear()
    for p in range (0, len(args.featureTwo)):
        secondFeatures.append(args.featureTwo[p])
    verboseprint("Second Features: " + str(secondFeatures) + "\n""")

if args.subMode:
    submode = args.subMode
else:
    submode = 1

if args.output:
    fileOut = args.output
else:
    pass
        
# Function Declaration
def initOut(fileName, fileType, fileIndex):
    # Initialises output file
    if fileType == 'xls':
        if fileIndex == 0:
            excelSheet = Workbook()
            sheet1 = excelSheet.active
            sheet1.title = 'Analysis'
            # excelSheet = formatSheet(excelSheet, features)
            return excelSheet
    elif fileType == 'txt':
            textFile = open(fileName[:-4] + "_Parsed.txt", "w+")
            return textFile

def textLineParsing(file):
    fileLines = []
    with open (file, 'rt') as in_file:
        for line in in_file:
            fileLines.append(line)
    return fileLines

def lineDictionary(line):
    wordHits = dict()
    words = line.split()
    for word in words:
        if word in wordHits:
            wordHits[word] += 1
        else:
            wordHits[word] = 1
    return(wordHits)

if __name__ == '__main__':
    for inputFile in openFile:
        verboseprint("Looking at file number " + str(inputFile) + " in folder...") 
        parsedFile = initOut(inputFile, fileOutput, openFile.index(inputFile))
        # fileName = os.path.basename(inputFile[:-4])
        fileLines = textLineParsing(inputFile)
        for i in range(len(fileLines)):
            wordLineDict = lineDictionary(fileLines[i].lower())
            for tag in tags:
                if tag in wordLineDict:
                    
                    # MODE 0
                    if scriptMode == 0:
                        verboseprint ("I found " + tag + " on line " + str(i))
                        hits += wordLineDict[tag]
                        if considerduplicates:
                            tagsInLine = wordLineDict[tag]
                        else:
                            tagsInLine = 1
                            ignoredTags += wordLineDict[tag] - tagsInLine
                        for k in range (tagsInLine):
                            verboseprint ("I found " + tag + " on line " + str(i))
                            min = i - span
                            max = i + span
                            for line in range(min, max + 1):
                                if line >= 0 and line < len(fileLines):
                                    if line == i: parsedFile.write("-")
                                    parsedFile.write(str(line))
                                    parsedFile.write(" " + fileLines[line])
                            printedSpans += 1
                            parsedFile.write("\n")
    
    verboseprint("I found " + str(hits) + " tags in total.")
    verboseprint("I printed " + str(printedSpans) + " spans in the text file.")
    verboseprint("I ignored " + str(ignoredTags) + " tags in total.")


            
        

# for inputFile in openFile:
    
    # inputFile = path
    # This should accept both .txt and .xls outputs
    # result = open(inputFile[:-4] + "_Parsed.txt", "w+")

#     for i, line in enumerate(open(inputFile)):
#         for var in tags:
#             resetTag = 0
#             if re.search(r'\b' + var + '\\b', line):

#                 if scriptMode == 0: # Mode 0
#                     verboseprint ("I found " + var + " on line " + str(i))
#                     tagsFound += 1
#                     min = i - span
#                     max = i + span
#                     for e, line in enumerate(open(inputFile)):
#                         while e > min and e < max:
#                             if len(lineCount) >= 1:
#                                 spaceSeeker = int(e) - int(lineCount[-1])
#                                 if spaceSeeker >= 2:
#                                     result.write("\n")
#                             if considerduplicates and e in lineCount:
#                                 break
#                             lineCount.append(e)
#                             result.write(str(e))
#                             result.write(" " + line)
#                             break
#                         if e == max:
#                             if considerduplicates == False:
#                                 result.write("\n")
#                             break

#                 elif scriptMode == 1: # Mode 1
#                     verboseprint ("I found that line " + str(i) + " contains one or more " + var)
#                     tagsFound += 1
#                     min = i - 2
#                     tag = i
#                     max = i + 3
#                     for s, line in enumerate(open(inputFile)):
#                         if submode == 1: # Submode 1 -> TODO explicit copy past to fix
#                             if s == tag:
#                                 for secondFeature in secondFeatures:
#                                     if secondFeature == var:
#                                         counts = dict()
#                                         words = line.split()
#                                         for word in words:
#                                             if word in counts:
#                                                 counts[word] += 1
#                                             else:
#                                                 counts[word] = 1
#                                         try:
#                                             verboseprint("I found " + str(counts[secondFeature]) + " occurrances of \"" + secondFeature + "\" in line " + str(s))
#                                             if counts[secondFeature] > 1:
#                                                 featureFound = True
#                                             else:
#                                                 verboseprint("There is no \"" + secondFeature + "\" in line " + str(s) + " other than the main searched tag")
#                                         except:
#                                             verboseprint("There is no \"" + secondFeature + "\" in line " + str(s))
#                                     else:
#                                         if re.search(r'\b' + secondFeature + '\\b', line):
#                                             featureFound = True
#                                             verboseprint("I found \"" + secondFeature + "\" in line " + str(s))
#                                         else:
#                                             verboseprint("There is no \"" + secondFeature + "\" in line " + str(s))
#                             if s == tag + 2:
#                                 for secondFeature in secondFeatures:
#                                     if re.search(r'\b' + secondFeature + '\\b', line):
#                                         featureFound = True
#                                         verboseprint("I found \"" + secondFeature + "\" in line " + str(s))
#                                     else:
#                                         verboseprint("There is no \"" + secondFeature + "\" in line " + str(s))
#                                 if featureFound == True:                            
#                                     for k, line in enumerate(open(inputFile)):
#                                         while k > min and k < max:
#                                             if len(lineCount) >= 1:
#                                                 spaceSeeker = int(k) - int(lineCount[-1])
#                                                 if spaceSeeker >= 2:
#                                                     result.write("\n")
#                                             # if considerduplicates and i in lineCount:
#                                             #     break
#                                             lineCount.append(k)
#                                             result.write(str(k))
#                                             result.write(" " + line)
#                                             break
#                                         if k == max:
#                                             # if considerduplicates == False:
#                                             result.write("\n")
#                                             featureFound = False
#                                             verboseprint("")
#                                             break
#                                 else:
#                                     verboseprint("")
#                                 break
#                         elif submode == 2: # Submode 2 -> TODO explicit copy past to fix
#                             if s == tag:
#                                 for secondFeature in secondFeatures:
#                                     if secondFeature == var:
#                                         counts = dict()
#                                         words = line.split()
#                                         for word in words:
#                                             if word in counts:
#                                                 counts[word] += 1
#                                             else:
#                                                 counts[word] = 1
#                                         try:
#                                             verboseprint("I found " + str(counts[secondFeature]) + " occurrances of \"" + secondFeature + "\" in line " + str(s))
#                                             if counts[secondFeature] > 1:
#                                                 featureFound = True
#                                             else:
#                                                 verboseprint("There is no \"" + secondFeature + "\" in line " + str(s) + " other than the main searched tag")
#                                         except:
#                                             verboseprint("There is no \"" + secondFeature + "\" in line " + str(s))
#                                     else:
#                                         if re.search(r'\b' + secondFeature + '\\b', line):
#                                             featureFound = True
#                                             verboseprint("I found \"" + secondFeature + "\" in line " + str(s))
#                                         else:
#                                             verboseprint("There is no \"" + secondFeature + "\" in line " + str(s))
#                             if s == tag + 1:
#                                 for secondFeature in secondFeatures:
#                                     if re.search(r'\b' + secondFeature + '\\b', line):
#                                         featureFound = True
#                                         verboseprint("I found \"" + secondFeature + "\" in line " + str(s))
#                                     else:
#                                         verboseprint("There is no \"" + secondFeature + "\" in line " + str(s))
#                                 if featureFound == True:                            
#                                     for k, line in enumerate(open(inputFile)):
#                                         while k > min and k < max:
#                                             if len(lineCount) >= 1:
#                                                 spaceSeeker = int(k) - int(lineCount[-1])
#                                                 if spaceSeeker >= 2:
#                                                     result.write("\n")
#                                             # if considerduplicates and i in lineCount:
#                                             #     break
#                                             lineCount.append(k)
#                                             result.write(str(k))
#                                             result.write(" " + line)
#                                             break
#                                         if k == max:
#                                             # if considerduplicates == False:
#                                             result.write("\n")
#                                             featureFound = False
#                                             verboseprint("")
#                                             break
#                                 else:
#                                     verboseprint("")
#                                 break
#                         elif submode == 3: # Submode 3 -> TODO explicit copy past to fix
#                             if s == tag:
#                                 for secondFeature in secondFeatures:
#                                     if secondFeature == var:
#                                         counts = dict()
#                                         words = line.split()
#                                         for word in words:
#                                             if word in counts:
#                                                 counts[word] += 1
#                                             else:
#                                                 counts[word] = 1
#                                         try:
#                                             verboseprint("I found " + str(counts[secondFeature]) + " occurrances of \"" + secondFeature + "\" in line " + str(s))
#                                             if counts[secondFeature] > 1:
#                                                 featureFound = True
#                                             else:
#                                                 verboseprint("There is no \"" + secondFeature + "\" in line " + str(s) + " other than the main searched tag")
#                                         except:
#                                             verboseprint("There is no \"" + secondFeature + "\" in line " + str(s))
#                                     else:
#                                         if re.search(r'\b' + secondFeature + '\\b', line):
#                                             featureFound = True
#                                             verboseprint("I found \"" + secondFeature + "\" in line " + str(s))
#                                         else:
#                                             verboseprint("There is no \"" + secondFeature + "\" in line " + str(s))
#                             if s == tag + 1:
#                                 for secondFeature in secondFeatures:
#                                     if re.search(r'\b' + secondFeature + '\\b', line):
#                                         featureFound = True
#                                         verboseprint("I found \"" + secondFeature + "\" in line " + str(s))
#                                     else:
#                                         verboseprint("There is no \"" + secondFeature + "\" in line " + str(s))
#                             if s == tag + 2:
#                                 for secondFeature in secondFeatures:
#                                     if re.search(r'\b' + secondFeature + '\\b', line):
#                                         featureFound = True
#                                         verboseprint("I found \"" + secondFeature + "\" in line " + str(s))
#                                     else:
#                                         verboseprint("There is no \"" + secondFeature + "\" in line " + str(s))
#                                 if featureFound == True:                            
#                                     for k, line in enumerate(open(inputFile)):
#                                         while k > min and k < max:
#                                             if len(lineCount) >= 1:
#                                                 spaceSeeker = int(k) - int(lineCount[-1])
#                                                 if spaceSeeker >= 2:
#                                                     result.write("\n")
#                                             # if considerduplicates and i in lineCount:
#                                             #     break
#                                             lineCount.append(k)
#                                             result.write(str(k))
#                                             result.write(" " + line)
#                                             break
#                                         if k == max:
#                                             # if considerduplicates == False:
#                                             result.write("\n")
#                                             featureFound = False
#                                             verboseprint("")
#                                             break
#                                 else:
#                                     verboseprint("")
#                                 break
#                         # if s == max:
#                         #     featureFound = False
#                         #     verboseprint("")
# verboseprint ("I found a total of " + str(tagsFound) + " tags")
# verboseprint(tagsDict)
# result.close()