from sys import argv 
from os.path import exists 

script, inputfile, outputfile = argv
_INPUTFILE = open(inputfile); _OUTPUTFILE = _INPUTFILE.read()
raw_input()
outFile = open(outputfile, "w")
outFile.write(_OUTPUTFILE)

