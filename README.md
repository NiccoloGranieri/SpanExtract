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
If you would like to change the range of lines saved around the found markers, just add a number after the _python_ command. For example, if I wanted only 3 lines before and after the marker, I would type:

```bash
python SpanExtract.py my_file_name.txt 3
```

If you would like to search for your own markers, just type them one after the other after the number that sets the lines saved, in inverted commas.  For example, if I wanted to set the saved lines to 6 and look for the markers:

- ((smile))
- giggle
- (hug)

then you would type:

```bash
python SpanExtract.py my_file_name.txt 6 '((smile))' 'giggle' '(hug)'
```