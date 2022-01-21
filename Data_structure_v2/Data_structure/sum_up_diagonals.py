def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    i=0
    total = 0
    while i <2:
        for j in range(len(matrix)):
            if i ==0:
                total +=matrix[j][j]
            else:
                total +=matrix[len(matrix)-1-j][j]
        i+=1
    return total
m1 = [[1,   2],[30, 40]]
m2 = [[1, 2, 3],[4, 5, 6],[7, 8, 9],]
print(sum_up_diagonals(m1))
print(sum_up_diagonals(m2))
