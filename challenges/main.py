

def print_matrix_horz():
    '''
        Challenge1: Print matrix in horz order
    '''
    matrix = [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

    # Method 1
    results = []
    for item in matrix:
        for i in item:
            results.append(i)
    print ','.join(map(str, results))

    # Method 2
    results = []
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[0])):
            results.append(matrix[i][j])
    print ','.join(map(str, results))


def print_matrix_vert():
    '''
        Challenge2: Print matrix in vertical order
    '''
    matrix = [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

    # Method 1
    results = []
    for j in xrange(len(matrix[0])):
        for i in xrange(len(matrix)):
            results.append(matrix[i][j])
    print ','.join(map(str, results))

    # Method 2
    results = []
    for i in xrange(len(matrix[0])):
        results.extend([item[i] for item in matrix])
    print ','.join(map(str, results))


def print_top_right(matrix, x1, y1, x2, y2):
    for x in range(x1, x2+1):
        print matrix[y1][x]
    for y in range(y1+1, y2+1):
        print matrix[y][x2]

    if x2-x1 and y2-y1:
        print_bottom_left(matrix, x1, y1+1, x2-1, y2)

def print_bottom_left(matrix, x1, y1, x2, y2):
    for x in range(x2, x1-1, -1):
        print matrix[y2][x]
    for y in range(y2-1, y1-1, -2):
        print matrix[y][x1]

    if x2-x1 and y2-y1:
        print_top_right(matrix, x1+1, y1, x2, y2-1)

def print_matrix_spiral():
    '''
        Challenge3: Print matrix in spiral order
        0, 0, 0, 0, 0
        0, 1, 2, 3, 4
        0, 2, 4, 6, 8
        0, 1, 2, 3, 4
    '''
    matrix = [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 1, 2, 3, 4]]
    COL = len(matrix[0])
    ROW = len(matrix)
    print_top_right(matrix, 0, 0, COL-1, ROW-1)


def main():
    '''
    print_matrix_horz()
    print_matrix_vert()
    '''
    print_matrix_spiral()

if __name__ == "__main__":
    main()
