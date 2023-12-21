def submatrix_with_particular_sum(matrix):
    return [
        [
            [
                row[row.index(row[i])]
                for i in range(row.index(row[i]))
            ]
            for row in matrix
        ]
        for row in matrix
    ]
