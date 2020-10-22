import os

def fileOpener(fileName, startGene, endGene):
    print("Retriving genome from: " + fileName)
    file = open(fileName, "r")

    genome = file.read()
    genome = genome.replace("\n", "")

    print("Grabbing desired gene from the genome.")

    gene = genome[startGene:endGene]

    print("This is the gene: \n" + gene)

    return gene