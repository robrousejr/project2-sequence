import fileOpener as fileReader
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

nsp1Covid = fileReader.fileOpener("genes/covidGenome.txt", 266, 805)
nsp1MERS = fileReader.fileOpener("genes/mersGenome.txt", 279, 857)

# Print out alignment
for a in pairwise2.align.globalxx(nsp1Covid, nsp1MERS):
    print(format_alignment(*a))