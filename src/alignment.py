import fileOpener as fileReader
import functions as functions
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

nsp1Covid = fileReader.fileOpener("genes/covidGenome.txt", 266, 805)
nsp1MERS = fileReader.fileOpener("genes/mersGenome.txt", 279, 857)

print("\nPrinting out alignment\n")

# Print out alignment
for a in pairwise2.align.localxx(nsp1Covid, nsp1MERS):
    print(format_alignment(*a))