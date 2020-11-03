import fileOpener as fileReader
from functions import *

nsp1Covid = fileReader.fileOpener("genes/covidGenome.txt", 266, 805)
nsp1MERS = fileReader.fileOpener("genes/mersGenome.txt", 279, 857)

# Run local alignment
localAlignment = LocalAlignment(nsp1Covid, nsp1MERS, None)
localAlignment.local_align()