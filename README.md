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

- Type the _python_ command, followed by the name of the Span Extract script and the name of your file, including extensions. If the script name is unchanged:

```bash
python SpanExtract.py my_file_name.txt
```

- This will generate a .txt file called _Parsed.txt_ that contains a span of 10 lines around each marker found. In the original script the markers are different kinds of laughter in a transcript. (LAUGHS, laughs, laughing, chuckles, chuckling, hehe, heh, ehh, thh)

#### _Optional_

--mode = Switches modes of the script.
    0. Looks for tags and extracts lines around it.
    1. Looks for tags and extracts lines around it only if a second feature is found in the surrounding lines.
parser.add_argument("--mode", help="sets the mode of the script", type=int)
--verbose = Enables verbose mode. Calling it makes it true, not calling it makes it false.
--span = sets the span of the lines to extract. Default is 6 (5 + 1 + 5). Applies only to mode 0.
--duplicates = sets the script to print lines that have been printed before. Calling it makes it true, not calling it makes it false
--tags = sets the tags to search in the text. Applies to both modes.
--featureTwo = sets the second feature to search around the tags. Applies only to mode 1.

##### _Number of Lines in Span_
If you would like to change the range of lines saved around the found markers, just add a number after the _python_ command. For example, if I wanted only 3 lines before and after the marker, I would type:

```bash
python SpanExtract.py my_file_name.txt 3
```

##### _Changing the output mode_
If you would like to set the script to run, search, and output lines taking into account duplicates, and removing them, resulting in a file with no duplicate lines, you should set the mode to 0. To do so, just put a zero after the number that sets the lines saved.

```bash
python SpanExtract.py my_file_name.txt 3 0
```

If instead, you would like to set the script to run, search, and output lines not taking into account duplicates, and printing the span every time a marker is found, you should set the mode to 1. To do so, just put a one after the number that sets the lines saved.

```bash
python SpanExtract.py my_file_name.txt 3 1
```

#### _Looking for a second feature within the line of the node and the one after the next_
This fourth arguement changes radically the behaviour of the script. By setting the third argument to 1, you ask the script not only to search for lines containing the desired markers, but only output them if the the found span a second feature is found. The second feature, for now, is hard coded, and is the word 'you'.

```bash
python SpanExtract.py my_file_name.txt 3 1 1
```

*Note*
This mode will effectively override both the span and mode arguments previously explained. This mode will always output 4 lines: the line where the marker has been found, one previous line, and the following two lines.

##### _Searching for Personalised Markers_

If you would like to search for your own markers, just type them one after the mode, in inverted commas.  For example, if I wanted to set the saved lines to 6 and look for the markers:

- ((smile))
- giggle
- (hug)

then you would type:

```bash
python SpanExtract.py my_file_name.txt 6 0 0 '((smile))' 'giggle' '(hug)'
```