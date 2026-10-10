# N-Queens Problem Solver with Backtracking and branch and bound approach 

def solveNQueens(n):
    col = set()        # stores used columns
    posDiag = set()    # stores r+c diagonals (/)
    negDiag = set()    # stores r-c diagonals (\)

    res = []
    board = [['.' for _ in range(n)] for _ in range(n)]

    def backtrack(r):
        # if all rows are filled → store solution
        if r == n:
            res.append([''.join(row) for row in board])
            return

        for c in range(n):  # try each column
            # check if position is safe
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue

            # place queen
            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = 'Q'

            backtrack(r+1)  # move to next row

            # remove queen (backtrack)
            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = '.'

    backtrack(0)
    return res


def printSolutions(boards):
    i = 1
    for board in boards:
        print(f"Solution {i}:")
        for row in board:
            print(' '.join(row))
        print()
        i += 1


# main

if __name__ == "__main__":
    boards = solveNQueens(4)
    printSolutions(boards)