class WordMatch:

    def __init__(self, word, start, end, direction):
        self.word = word
        self.start = start
        self.end = end
        self.direction = direction

    def __str__(self) -> str:
        return self.word + " from " + str(self.start) + " to " + str(self.end) + " (direction: " + self.direction + ")"

