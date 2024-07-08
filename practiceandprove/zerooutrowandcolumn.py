def zeroOutRowAndCol(matrix):
    rownum = len(matrix)
    colnum = len(matrix[0])

    row_dict_with_zeros = {}
    col_dict_with_zeros = {}

    for i in range(rownum):
        for j in range(colnum):
            if matrix[i][j] == 0:
                row_dict_with_zeros[i] = 1
                col_dict_with_zeros[j] = 1

    # Zeroing out rows based on position

    for i in row_dict_with_zeros.keys():
        for j in range(colnum):
            matrix[i][j] = 0

    # Zeroing out columns based on position

    for j in col_dict_with_zeros.keys():
        for i in range(rownum):
            matrix[i][j] = 0

    return matrix


def main():
    result = zeroOutRowAndCol([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
    print("Zeroed out matrix:")

    for row in result:
        print(row)


if __name__ == "__main__":
    main()
