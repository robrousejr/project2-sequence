import fileOpener as fileReader
from LocalAlignment import LocalAlignment

#the nsp1 gene in covid is located from 266 to 805
#the nsp1 gene in MERS is located from 279 to 857
#the nsp1 gene is SARS is located from 265 to 804

nsp1Covid = fileReader.fileOpener("genes/covidGenome.txt", 266, 805)
nsp1MERS = fileReader.fileOpener("genes/mersGenome.txt", 279, 857)

# Run local alignment on MERS and Covid
localAlignment = LocalAlignment(nsp1Covid, nsp1MERS, None)
localAlignment.local_align()

#Run local alignment on SARS and Covid

nsp1SARS = fileReader.fileOpener("genes/sarsGenome.txt", 265, 804)
localAlignment = LocalAlignment(nsp1Covid, nsp1SARS, None)
localAlignment.local_align()