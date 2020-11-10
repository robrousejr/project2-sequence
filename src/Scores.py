# Gap, Match, Mismatch (-2, 1, -1)
class Scores():
    def __init__(self, gap, match, mismatch):
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