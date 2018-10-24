import puzzle

if __name__ == '__main__':
    print("Welcome to Word Search Solver.")
    puzzle = puzzle.Puzzle(date="2018-10-20")
    for word in puzzle.words:
        print(puzzle.match(word))
