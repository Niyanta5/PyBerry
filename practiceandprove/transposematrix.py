def transposematrix(matrix):
    matrixlen = len(matrix)

    for i in range(matrixlen):
        for j in range(i + 1, matrixlen):
            # Corrected swap operation
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


def main():
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Original Matrix:")

    for row in mat1:
        print(row)

    print("\nTransposed Matrix:")

    transposed = transposematrix(mat1)

    for row in transposed:
        print(row)


if __name__ == "__main__":
    main()
