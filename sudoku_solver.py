from pprint import pprint


def find_next_empty(puzzle):
    """
    finds the next row, col on the puzzle that's not filled yet
    :param puzzle: initial sudoku board represented by list of lists
    :return: row, col tuple (or (None, None) if there is none)
    """

    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == -1:
                return row, column

    return None, None


def is_valid(puzzle, guess, row, col):
    """
    figures out whether the guess at the row/col of the puzzle is a valid guess
    :param puzzle: initial sudoku board represented by list of lists
    :param guess: current number
    :param row: row in a puzzle
    :param col: column in a puzzle
    :return: True or False
    """

    row_vals = puzzle[row]
    # if we've repeated, then our guess is not valid
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    # if we've repeated, then our guess is not valid
    if guess in col_vals:
        return False

    # the inner square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True


def solve_sudoku(puzzle):
    """
    solves sudoku using backtracking and mutates puzzle to be the solution (if solution exists)
    :param puzzle: initial sudoku board represented by list of lists
    where each inner list is a row in our sudoku puzzle
    :return: whether a solution exists
    """
    row, col = find_next_empty(puzzle)

    # if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if solve_sudoku(puzzle):
                return True

        # if it is not valid or if nothing gets returned true, then we need to backtrack and try a new number
        puzzle[row][col] = -1

    # if none of the numbers that we try work, then this puzzle is unsolvable
    return False


if __name__ == '__main__':
    example_board = [
        [3, 9, -1, -1, 5, -1, -1, -1, -1],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],

        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],

        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
