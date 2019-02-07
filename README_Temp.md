# Submode Alpha Script (For Selina's eyes only)

The command used to launch the script is always the same:

`python3 SpanExtract_SELINA.py --fileParsing ViMELF_01SB32FL06_final_osl_1st.txt --mode 1 --tags 'we_#0' --featureTwo 'you' 'your' 'yours' --subMode 1 --verbose`

with the addition of the command line argument:

`--subMode`

subMode accepts a number between 1 and 3 and changes the behaviour of the search function related to the second Feature.

## subMode 1

<span style="color:red">A1</span>   --  _mainTag_

B1

<span style="color:red">A2</span>

B2

Considering that the main tag has been found in A1, the second features will be seeked in lines A1 and A2 only.

## subMode 2

<span style="color:red">A1</span>   --  _mainTag_

<span style="color:red">B1</span>

A2

B2

Considering that the main tag has been found in A1, the second features will be seeked in lines A1 and B1 only.

## subMode 3

<span style="color:red">A1</span>   --  _mainTag_

<span style="color:red">B1</span>

<span style="color:red">A2</span>

B2

Considering that the main tag has been found in A1, the second features will be seeked in lines A1, B1 and A2.

# Bug Fixes

Now the script is able to deal also with multiple instances of the same tag searched. (eg. --tags 'we_#0', --featureTwo 'we_#0')