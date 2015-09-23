

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


def main():
    print_matrix_horz()
    print_matrix_vert()

if __name__ == "__main__":
    main()
