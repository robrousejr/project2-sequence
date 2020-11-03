import numpy as np

# Gap, Match, Mismatch (-2, 1, -1)
class Scores():
    def __init__(self, match, mismatch, gap):
        self.match = match
        self.mismatch = mismatch
        self.gap = gap
    def __str__(self):
        return 'gap, match, mismatch ({self.gap}, {self.match}, {self.mismatch})'.format(self=self)

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
