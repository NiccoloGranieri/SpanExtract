# Span Extract

A tool to extract a span of lines around a found marker in a text file.

## Easy how-to guide

### _Mac / UNIX_

It is reccomended, for ease of use, to store both the script and the text file to search in the same folder before following this step-by-step guide.

- Open the terminal
- Navigate using the _cd_ command to the folder where both the files are stored. For example, if your files are both stored on the Desktop:

```bash
cd /Users/_your_user_name_/Desktop
```

- Type the _python3_ command, followed by the name of the Span Extract script, the command line argument _--fileParsing_ and the name of your file, including extensions. If the script name is unchanged, your command will look something like this:

```bash
python3 SpanExtract.py --fileParsing myFileName.txt
```

- This will generate a .txt file called _myFileName\_Parsed.txt_ that contains a span of 10 lines around each marker found. In the script, the default markers are different kinds of laughter found in a transcript. (LAUGHS, laughs, laughing, chuckles, chuckling, hehe, heh, ehh, thh)

### _Optional Command Line Arguments_

The script allows to modify its behaviour through a series of command line arguments. Command line arguments are key words preceded by _"--"_ than set the script to behave in different ways. Below, a list of all the available command line arguments.

#### --mode
The _--mode_ command line argument, followed by a 0 or a 1, lets us switch between the different modes of the script. Mode 0 looks for tags and extracts lines around it. To set personalised markers, see the _--tags_ argument, to change the span of lines extracted, see the _--span_ argument, to take into consideration duplicate lines, see the _--duplicates_ argument.

```bash
python3 SpanExtract.py --fileParsing myFileName.txt --mode 0
```

Mode 1, looks for tags and extracts lines around it only if a second feature is found in the surrounding lines. To set personalised markers, see the _--tags_ argument, to take into consideration duplicate lines, see the _--duplicates_ argument.

```bash
python3 SpanExtract.py --fileParsing myFileName.txt --mode 1
```

#### --tags
If you would like to search for your own markers, use the _--tags_ command line argument and add them one after the other in inverted commas. For example, if I wanted to look for the markers:

- ((smile))
- giggle
- (hug)

I would type:

```bash
python3 SpanExtract.py --fileParsing myFileName.txt --mode 0 --tags '((smile))' 'giggle' '(hug)'
```

#### --span
If you would like to change the range of lines saved around the found markers, use the _--span_ command line argument followed by a number. For example, if I wanted only 3 lines before and after the marker, I would type:

```bash
python3 SpanExtract.py --fileParsing myFileName.txt --mode 0 --span 3
```
#### --duplicates
If you would like to set the script to run, search, and output lines taking into account duplicates, and removing them, resulting in a file with no duplicate lines, you should call the _--duplicates_ command line argument. This argument is valid only in mode 0.

```bash
python3 SpanExtract.py --fileParsing myFileName.txt --mode 0 --duplicates
```

If instead, you would like to set the script to run, search, and output lines not taking into account duplicates, and printing the span every time a marker is found, you should set the mode to 1. To do so, just put a one after the number that sets the lines saved.

#### --featureTwo
When in _--mode 1_, there is also the possibility to change the second feature to seek in the span around the marker found. The second feature by default is _'you'_, but it can be changed to one or multiple features by calling the command line argument _--featuretwoTwo_.

```bash
python3 SpanExtract.py --fileParsing myFileName.txt --mode 1 --featureTwo 'his'
```

*Note*
This mode will effectively ignore any _--span_ or _--duplicates_ arguments previously explained. This mode will always output 4 lines: the line where the marker has been found, one previous line, and the following two lines.

#### --fileParsing and --folderParsing
One of these two arguments is essential for the script to run. _--fileParsing_ as previously explained, lets us set the .txt file to parse. _--folderParsing_ instead lets us iteratively run the script through all the .txt files in a specified folder. The syntax is the same for both, with the name of the txt file being called in the first instance, and the name of the folder in the second one with a forward slash _\/_ at the end.

```bash
python3 SpanExtract.py --fileParsing myFileName.txt
```

```bash
python3 SpanExtract.py --folderParsing myFolderName/
```

#### --verbose
This last command line arguement, when called, enables verbose mode. Verbose mode will print on the terminal windows a series of useful text relative to the parsing of the text file chosen. This mode is useful to enable when trying to figure out why a certain file is being parsed a certain way, or to check that the process is running smoothly.

```bash
python3 SpanExtract.py --fileParsing myFileName.txt --verbose
```

