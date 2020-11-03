import fileOpener as fileReader
from functions import *

nsp1Covid = fileReader.fileOpener("genes/covidGenome.txt", 266, 805)
nsp1MERS = fileReader.fileOpener("genes/mersGenome.txt", 279, 857)

print("\nPrinting out alignment\n")

localAlignment = LocalAlignment(nsp1Covid, nsp1MERS, None)
