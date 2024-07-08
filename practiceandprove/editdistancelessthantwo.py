def isDistanceLessThanTwo(strA, strB):
    lenA, lenB = len(strA), len(strB)

    if abs(lenA - lenB) > 1:
        return False

    if strA == strB:
        return False

    # check if the string are of same length and consider possible case for one replacement

    if lenA == lenB:
        distance = 0

        for char in range(lenA):
            if strA[char] != strB[char]:
                distance += 1

                if distance > 1:
                    return False

        return True

    # Ensure strA is the shorter string

    if lenA > lenB:
        strA, strB = strB, strA

    # check if strA can be transformed into strB by one insertion or deletion

    i = 0
    j = 0

    while i < len(strA) and j < len(strB):
        if strA[i] != strB[j]:
            if i != j:
                return False
            j += 1

        else:
            i += 1
            j += 1

    return True
