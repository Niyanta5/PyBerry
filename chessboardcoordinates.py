def getsquarecolor(square):
    column = square[0]  # a from a1
    row = square[1]  # 1 from a1

    # converting column letter to a number
    column_number = ord(column) - ord("a") - 1
    row_number = int(row)

    return (column_number + row_number) % 2


def same_color(square1, square2):
    color1 = getsquarecolor(square1)
    color2 = getsquarecolor(square2)

    return color1 == color2


def main():
    color1 = "a2"
    color2 = "b2"
    result = same_color(color1, color2)

    print(result)


main()
