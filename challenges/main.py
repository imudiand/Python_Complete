

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


def print_top_right(matrix, x1, y1, x2, y2, result):
    for x in range(x1, x2+1):
        result.append(matrix[y1][x])
    for y in range(y1+1, y2+1):
        result.append(matrix[y][x2])

    if x2-x1 and y2-y1:
        print_bottom_left(matrix, x1, y1+1, x2-1, y2, result)

def print_bottom_left(matrix, x1, y1, x2, y2, result):
    for x in range(x2, x1-1, -1):
        result.append(matrix[y2][x])
    for y in range(y2-1, y1-1, -2):
        result.append(matrix[y][x1])

    if x2-x1 and y2-y1:
        print_top_right(matrix, x1+1, y1, x2, y2-1, result)

def print_matrix_spiral():
    '''
        Challenge3: Print matrix in spiral order
        0, 0, 0, 0, 0
        0, 1, 2, 3, 4
        0, 2, 4, 6, 8
        0, 1, 2, 3, 4
    '''
    result = []
    matrix = [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 1, 2, 3, 4]]
    COL = len(matrix[0])
    ROW = len(matrix)
    print_top_right(matrix, 0, 0, COL-1, ROW-1, result)
    print ' '.join(map(str, result))



def print_matrix_diagonal():
    '''
        Challenge4: Print matrix in diagonal order
    Input:
        0, 0, 0, 0, 0
        0, 1, 2, 3, 4
        0, 2, 4, 6, 8
        0, 1, 2, 3, 4

    Result:
        0
        0 0
        0 1 0
        0 2 2 0
        1 4 3 0
        2 6 4
        3 8
        4
    '''
    matrix = [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 1, 2, 3, 4]]
    result = []

    COL = len(matrix[0])
    ROW = len(matrix)
    for line in range(ROW+COL):
        start_col = max(0, line-ROW)
        count = min(line, (COL-start_col), ROW);

        for j in range(count):
            result.append(matrix[min(ROW, line)-j-1][start_col+j])
    print result




def main():
    '''
    print_matrix_horz()
    print_matrix_vert()
    print_matrix_spiral()
    '''
    print_matrix_diagonal()

if __name__ == "__main__":
    main()
