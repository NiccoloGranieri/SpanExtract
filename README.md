# Span Extract

A tool to extract a span of lines around a found marker in a text file.

## Easy how-to guide

### _Mac / UNIX_

It is reccomended, for ease of use, to store both the script and the text file to search in the same folder before following this step-by-step guide.

- Open the terminal
- Navigate using the _cd_ command to the folder where both the files are stored. For example, if your files are both stored on the Desktop:
~~~~
cd /Users/_your_user_name_/Desktop
~~~~
- Type the _python_ command, followed by the name of the Span Extract script and the name of your file, including extensions. If the script name is unchanged:
~~~~
python SpanExtract.py my_file_name.txt
~~~~
- This will generate a .txt file called _Parsed.txt_ that contains a span of 10 lines around each marker found. In the original script the markers are different kinds of laughter in a transcript. (LAUGHS, laughs, laughing, chuckles, chuckling, hehe, heh, ehh, thh)