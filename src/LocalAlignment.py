from Scores import *
from functions import createMatrix

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

        bestScore = 0
        maxLocation = (0,0)

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
                if matrix[i][j] >= bestScore:
                    bestScore = matrix[i][j]
                    maxLocation = (i,j)

        print("Scoring: " + str(self.scores))
        print("Optimal Score =", bestScore)
        print("Max location in matrix =", maxLocation)

        # Return the score and optimal location
        return bestScore, maxLocation