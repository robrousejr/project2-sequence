import fileOpener as fileReader
from Bio import pairwise2

nsp1Covid = fileReader.fileOpener("genes/covidGenome.txt", 266, 805)
nsp1MERS = fileReader.fileOpener("genes/mersGenome.txt", 279, 857)