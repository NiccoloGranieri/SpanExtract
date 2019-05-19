import os
import sys
import re
import argparse
import Tags2Excel

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
lastLinePrinted = -1
lastSpanPrinted = -1

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

secondFeatures = ['((laughs))', '((laughing))', '((chuckles))', '((chuckling))', '((hehe))', '((heh))', '((ehh))', '((thh))']

if args.featureTwo:
    secondFeatures.clear()
    for p in range (0, len(args.featureTwo)):
        secondFeatures.append(args.featureTwo[p])
    verboseprint("Second Features: " + str(secondFeatures) + "\n""")

if args.subMode:
    submode = args.subMode
else:
    submode = 1.1

if args.output:
    fileOut = args.output
else:
    pass
        
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

def identifySubmode(modeParser):
    if modeParser == 1:
        dictsToParse = [hitLineDict, lastLineDict]
        return dictsToParse
    elif modeParser == 2:
        dictsToParse = [hitLineDict, nextLineDict]
        return dictsToParse
    elif modeParser == 3:
        dictsToParse = [hitLineDict, nextLineDict, lastLineDict]
        return dictsToParse

def lookingForFeatureTwo(dictsToSearch, secondFeatures):
    for secondFeature in secondFeatures:
        for d in range(0, len(dictsToParse)):
            if secondFeature in dictsToParse[d]:
                verboseprint ("    I found " + secondFeature + " around line  " + str(i))
                return True
    return False

if __name__ == '__main__':
    for inputFile in openFile:
        verboseprint("Looking at file number " + str(inputFile) + " in folder...") 
        parsedFile = initOut(inputFile, fileOutput, openFile.index(inputFile))
        # fileName = os.path.basename(inputFile[:-4])
        fileLines = textLineParsing(inputFile)
        for i in range(len(fileLines)):
            hitLineDict = lineDictionary(fileLines[i].lower())
            for tag in tags:
                if tag in hitLineDict:
                    hits += hitLineDict[tag]
                    
                    # MODE 0
                    if scriptMode == 0:
                        verboseprint ("I found " + tag + " on line " + str(i))
                        min = i - span
                        max = i + span
                        if considerduplicates == False:
                            tagsInLine = hitLineDict[tag]
                        else:
                            tagsInLine = 1
                            ignoredTags += hitLineDict[tag] - tagsInLine
                        for k in range (tagsInLine):
                            verboseprint ("I found " + tag + " on line " + str(i))
                            for line in range(min, max + 1):
                                if line >= 0 and line < len(fileLines) and line not in lineCount:
                                    if considerduplicates:
                                        if line == min and lastLinePrinted < line and lineCount != []:
                                            parsedFile.write("\n")
                                        lineCount.append(line)
                                    parsedFile.write(str(line))
                                    parsedFile.write(" " + fileLines[line])
                                    lastLinePrinted = line
                            if considerduplicates == False:
                                parsedFile.write("\n")
                            printedSpans += 1
                                    
                    # MODE 1 INCLUDING SUBMODES
                    elif scriptMode == 1:
                        min = i - 1
                        max = i + 2
                        if i < len(fileLines) - 1: nextLineDict = lineDictionary(fileLines[i+1].lower())
                        if i < len(fileLines) - 2: lastLineDict = lineDictionary(fileLines[i+2].lower())
                        dictsToParse = identifySubmode(submode)
                        tagsInLine = 1
                        ignoredTags += hitLineDict[tag] - tagsInLine
                        for k in range (tagsInLine):
                            verboseprint ("I found " + tag + " on line " + str(i))
                            if lookingForFeatureTwo(dictsToParse, secondFeatures):
                                if considerduplicates == True and i == lastSpanPrinted:
                                    pass
                                else:
                                    for line in range(min, max + 1):
                                        if line >= 0 and line < len(fileLines) and line not in lineCount:
                                            parsedFile.write(str(line))
                                            parsedFile.write(" " + fileLines[line])
                                    parsedFile.write("\n")
                                    lastSpanPrinted = i
                                    printedSpans += 1
    verboseprint("I found " + str(hits) + " tags in total.")
    verboseprint("I printed " + str(printedSpans) + " spans in the text file.")
    verboseprint("I ignored " + str(ignoredTags) + " tags in total.")
    parsedFile.close()