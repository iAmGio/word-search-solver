import datetime
import webparser
import puzzleraw
import wordmatch


class Puzzle:

    now = datetime.datetime.now()

    def __init__(self, date=str(now.year) + "-" + str(now.month) + "-" + str(now.day), psid="100000252"):
        self.date = date
        url = "https://data.puzzlexperts.com/puzzleapp/data.php?psid=" + psid + "&date=" + date
        array = webparser.WebParser(url).parse_to_array()
        raw = puzzleraw.PuzzleRaw(array)
        pairs = raw.make_pairs()
        self.scheme = pairs[0]
        self.words = pairs[1]

    @staticmethod
    def find_indexes(line, char):
        indexes = []
        for i in range(0, len(line)):
            if line[i] is char:
                indexes.append(i)
        return indexes

    def find_occurrences(self, char):
        loc = []
        for i in range(len(self.scheme)):
            loc.append([i, self.find_indexes(self.scheme[i], char)])
        return loc

    def get_near(self, index, line_index):
        scheme = self.scheme
        near = []

        index_not_first = index > 0
        index_not_last = len(scheme) > line_index and index < len(scheme[line_index]) - 1
        line_not_first = line_index > 0
        line_not_last = line_index < len(scheme) - 1

        if index_not_first:
            near.append([index - 1, line_index, "left"])

        if index_not_last:
            near.append([index + 1, line_index, "right"])

        if line_not_first:
            near.append([index, line_index - 1, "up"])
            if index_not_first:
                near.append([index - 1, line_index - 1, "up,left"])
            if index_not_last:
                near.append([index + 1, line_index - 1, "up,right"])

        if line_not_last:
            near.append([index, line_index + 1, "down"])
            if index_not_first:
                near.append([index - 1, line_index + 1, "down,left"])
            if index_not_last:
                near.append([index + 1, line_index + 1, "down,right"])

        return near

    def find_near_occurrences(self, char, index, line_index):
        occurrences = []
        for near in self.get_near(index, line_index):
            if self.scheme[near[1]][near[0]] is char:
                occurrences.append(near)
        return occurrences

    def match_word_part(self, word_part, index, line_index, direction):
        if len(word_part) is 1:
            return [index, line_index]
        word_part = word_part[1:len(word_part)]
        switch = {
            "left": [line_index, index - 1],
            "right": [line_index, index + 1],
            "up": [line_index - 1, index],
            "up,left": [line_index - 1, index - 1],
            "up,right": [line_index - 1, index + 1],
            "down": [line_index + 1, index],
            "down,left": [line_index + 1, index - 1],
            "down,right": [line_index + 1, index + 1]
        }
        next_loc = switch[direction]
        try:
            slot = self.scheme[next_loc[0]][next_loc[1]]
            return self.match_word_part(word_part, next_loc[1], next_loc[0], direction) if slot is word_part[0] else False
        except IndexError:
            return False

    def match(self, word):
        if word[0] is " ":
            word = word[1:len(word)]
        formatted_word = word.replace(" ", "")
        first_char = formatted_word[0]
        for occurrence in self.find_occurrences(first_char):
            line_index = occurrence[0]
            for index in occurrence[1]:
                for near in self.find_near_occurrences(formatted_word[1], index, line_index):
                    match = self.match_word_part(formatted_word, index, occurrence[0], near[2])
                    if match:
                        return wordmatch.WordMatch(word, [index, line_index], [match[0], match[1]], near[2])
