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

# Create and name output file
result = open("Parsed.txt","w+")

# If a third argument is identified, that becomes the span
if len(sys.argv) == 3:
    span = int(sys.argv[2]) + 1
else:
    span = 6

tags = ['((LAUGHS))', '((laughs))', '((laughing))', '((chuckles))', '((chuckling))', '((hehe))', '((heh))', '((ehh))', '((thh))']

lineCount = []

for i, line in enumerate(search):
    for c in range (0,9):
        var = tags[c]
        if var in line:
            print ("I found " + var + " on line " + str(i))
            min = i - span
            max = i + span
            for i, line in enumerate(open(path)):
                while i > min and i < max:
                    if i in lineCount:
                        break
                    else:
                        lineCount.append(i)
                        result.write(str(i))
                        result.write(" " + line)
                        break
result.close()