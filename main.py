import puzzle

if __name__ == '__main__':
    print("Welcome to Word Search Solver.")
    puzzle = puzzle.Puzzle(date="2018-10-20")
    # TODO: Use words from the web page
    print(puzzle.match("FALL"))
