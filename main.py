import puzzle

if __name__ == '__main__':
    print("Welcome to Word Search Solver.")
    date = input("Puzzle date as yyyy-mm-dd (leave empty to use today's date): ")
    psid = input("PSID (leave empty to use the default one):")
    puzzle = puzzle.Puzzle(date=date, psid=psid)
    for word in puzzle.words:
        print(puzzle.match(word))
