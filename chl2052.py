import sys
temperatureMode = sys.argv [1]      # Gets argument 1

with open ("challenge.data","r") as rawFile:         #Reads file and gets value stripping charatures
   contents = rawFile.read().strip()
   contentsValue = float(contents)          #converts to integer decimal


if temperatureMode == "FtoC":
    temperatureCalculation = (contentsValue - 32 ) * 5 / 9  #If F to C then assign calculated celsius to temperatureCalculation
elif temperatureMode == "CtoF":
    temperatureCalculation = (contentsValue * 9 / 5 ) + 32  #If C to F then assign calculateed fahrenheit to temperatureCalculation

#print(f"{temperatureCalculation}")
with open ("challenge.out", "w") as outputFile:
    outputFile.write(str(temperatureCalculation))

print("use CLI type challenge.out")



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