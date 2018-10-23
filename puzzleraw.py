class PuzzleRaw:

    def __init__(self, array):
        self.array = array

    def extract_data(self):
        return self.array['cells'][0]['meta']['data']

    def split(self):
        array = self.extract_data().split('########')
        x = 0
        for i in reversed(array):
            if " at " in i:
                break
            else:
                x = x + 1
        array = array[4:len(array) - x]
        return list(filter(lambda member: "NOT SELECTED" not in member, array))

    def make_pairs(self):
        array = self.split()
        pairs = [[], []]
        for member in array:
            if member.isupper():
                pairs[0].append(member)
            else:
                name = member.split(" at ")[0]
                name = name[2:len(name)]
                pairs[1].append(name)
        return pairs
