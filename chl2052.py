
"""
open ("challenge.data","r") as rawFile:
   contents = rawFile.read()
"""
import sys                              # Imports sys module

arg = sys.argv [1]                      # Assigns arg the value of sys.argv[1] 

print(f"{arg}: {sys.argv.index(arg)}")  # Prints an f string with the value of arg then plain text ': ' then the index position of sys.argv where arg is located in the list

"""
Chanllenge
run py clg2052.py argument

import sys

assign argument 1 to challengeValue


if argument is FtoC then calculate
    value converted = (value - 32) * 5 / 9
else if argument is CtoF then calculate
    value converted = (value * 9 / 5 ) +32

Get value and write to file challenge.out

"""