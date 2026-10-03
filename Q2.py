# the queen at board[row][col]
def isSafe(mat, row, col):
    n = len(mat)

    #upper side
    for i in range(row):
        if mat[i][col]:
            return False

    # left side
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if mat[i][j]:
            return False
        i -= 1
        j -= 1

    # right side
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if mat[i][j]:
            return False
        i -= 1
        j += 1

    return True

def placeQueens(row, mat):
    n = len(mat)

    if row == n:
        return True


    for i in range(n):

        if isSafe(mat, row, i):
            mat[row][i] = 1
            if placeQueens(row + 1, mat):
                return True
            mat[row][i] = 0
    return False

# main
def queens():
    n = 8

    mat = [[0] * n for _ in range(n)]

    placeQueens(0, mat)

    return mat

if __name__ == "__main__":
    res = queens()
    for v in res:
        print(" ".join(map(str, v)))
