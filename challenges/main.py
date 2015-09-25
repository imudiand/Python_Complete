import re

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
        count = min(line, (COL-start_col), ROW)
        for j in range(count):
            result.append(matrix[min(ROW, line)-j-1][start_col+j])
    print result


def quicksort(array):
    """
        Quicksort - with extra memory
    """
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array


def qsort(array, start, end):
    if start >= end:
        return

    pivot, left = start, start
    right = end

    while left < right:
        while array[left] <= array[pivot]:
            left += 1
        while array[right] > array[pivot]:
            right -= 1
        if left < right:
            # swap
            array[left], array[right] = array[right], array[left]

    # swap pivot & right (right now points to lower num)
    array[right], array[pivot] = array[pivot], array[right]

    # Apply recursive on either sides
    qsort(array, start, right-1)
    qsort(array, right+1, end)


def quicksort_inplace():
    """
    Quicksort - with no extra memory
    """
    array = [12, 4, 5, 6, 7, 3, 1, 15]
    qsort(array, 0, len(array)-1)
    print array



code = {
        'a':2, 'b':3, 'c':5, 'd':7, 'e':11, 'f':13, 'g':17, 'h':19, 'i':23, 'j':29, 'k':31, 'l':37, 'm':41, 'n':43,
        'o':47, 'p':53, 'q':59, 'r':61, 's':67, 't':71, 'u':73, 'v':79, 'w':83, 'x':89, 'y':97, 'z':101,
        'A':2, 'B':3, 'C':5, 'D':7, 'E':11, 'F':13, 'G':17, 'H':19, 'I':23, 'J':29, 'K':31, 'L':37, 'M':41, 'N':43,
        'O':47, 'P':53, 'Q':59, 'R':61, 'S':67, 'T':71, 'U':73, 'V':79, 'W':83, 'X':89, 'Y':97, 'Z':101
    }


def anagrams():
    """
        Anagrams - Find anagrams in a large file
    """
    anagram_map = {}
    chunk_size = 1024
    with open('anagram_file.txt', 'rb') as infile:
        pattern = r"\S"
        regex = re.compile(r'[a-zA-Z]+')
        while(True):
            data = infile.read(chunk_size)
            if not data:
                break
            words = regex.findall(data)

            for word in words:
                anagram_num = reduce(lambda x,y: x*y, [code[c] for c in word])
                if anagram_num in anagram_map:
                    anagram_map[anagram_num].append(word)
                else:
                    anagram_map[anagram_num] = [word]

    for v in anagram_map.itervalues():
        if len(v) > 1:
            print ', '.join(v)

def regex_ip_address():
	"""
		Match an IP address
		===================
	"""
	num = r"([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
	pattern = r"^{0}\.{0}\.{0}\.{0}$".format(num)

	regex = re.compile(pattern)
	ip_addresses = ["255.255.255.255", "255.255.275.255", "255.255.255"]

	for ip in ip_addresses:
		match = regex.match(ip)
		if match:
			print "IS IP"
		else:
			print "NOT IP"



def main():
    '''
    print_matrix_horz()
    print_matrix_vert()
    print_matrix_spiral()
    print_matrix_diagonal()
    print quicksort(array=[12,4,5,6,7,3,1,15])
    quicksort_inplace()
    anagrams()
    '''
    regex_ip_address()


if __name__ == "__main__":
    main()
