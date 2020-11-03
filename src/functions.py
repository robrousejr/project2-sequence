# Creates zero filled matrix based on size of strains
def createMatrix(xSize, ySize):
    return [[0]*ySize for i in range(xSize)]
    

# Gap, Match, Mismatch (-2, 1, -1)
class Scores():
    def __init__(self, match, mismatch, gap):
        self.match = match
        self.mismatch = mismatch
        self.gap = gap
    def __str__(self):
        return 'gap, match, mismatch ({self.gap}, {self.match}, {self.mismatch})'.format(self=self)

    def matchchar(self, a,b):
        """Return the score for aligning character a with b"""
        assert len(a) == len(b) == 1
        if a==b:
            return self.match
        else:
            return self.mismatch

class LocalAlignment():
    def __init__(self, str1, str2, scores):
        self.str1 = str1
        self.str2 = str2
        if (type(scores) is Scores):
            self.scores = scores
        else:
            self.scores = Scores(-2, 1, -1) # Default values
    def __str__(self):
        return str(self.scores) + '\n{self.str1}\n{self.str2}'.format(self=self)

    # Maximizing local alignment function
    def local_align(self):
        
        # Create the matrix
        matrix = createMatrix(len(self.str1) + 1, len(self.str2) + 1)

        best = 0
        optloc = (0,0)

        # fill in matrix in the right order
        for i in range(1, len(self.str1)+1):
            for j in range(1, len(self.str2)+1):

                # the local alignment recurrance rule:
                matrix[i][j] = max(
                matrix[i][j-1] + self.scores.gap,
                matrix[i-1][j] + self.scores.gap,
                matrix[i-1][j-1] + self.scores.matchchar(self.str1[i-1], self.str2[j-1]),
                0
                )

                # track the cell with the largest score
                if matrix[i][j] >= best:
                    best = matrix[i][j]
                    optloc = (i,j)

        print("Scoring:", str(self.scores))
        print("Optimal Score =", best)
        print("Max location in matrix =", optloc)

        # Return the score and optimal location
        return best, optloc