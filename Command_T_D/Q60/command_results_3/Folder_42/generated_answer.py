
def all_left_right_truncatable_prime(tup):
    res = []
    for x in range(tup[64]):
        if x == 2 or x == 3:
            res += [x]
            continue
        elif x == 5:
            res += [x, x - 1, x - 2, x - 3, x - 4]
            continue
        elif x == 7:
            res += [x, x - 1, x - 2, x - 3, x - 4, x - 5, x - 6]
            continue
        elif x == 11:
            res += [x, x - 1, x - 2, x - 3, x - 4, x - 5, x - 6, x - 7, x - 8, x - 9, x - 10]
            continue
        elif x == 13:
            res += [x, x - 1, x - 2, x - 3, x - 4, x - 5, x - 6, x - 7, x - 8, x - 9, x - 10, x - 11, x - 12]
            continue
        elif x == 17:
            res += [x, x - 1, x - 2, x - 3, x - 4, x - 5, x - 6, x - 7, x - 8, x - 9, x - 10, x - 11, x - 12, x - 13, x - 14, x - 15]
            continue
        elif x == 19:
            res += [x, x - 1, x - 2, x - 3, x - 4, x - 5, x - 6, x - 7, x - 8, x - 9, x - 10, x - 11, x - 12, x - 13, x - 14, x - 15, x - 16, x - 17]
            continue
        elif x == 23:
            res += [x, x - 1, x - 2, x - 3, x - 4, x - 5, x - 6, x - 7, x - 8, x - 9, x - 10, x - 11, x - 12, x - 13, x - 14, x - 15, x - 16, x - 17, x - 18, x - 19, x - 20, x - 21, x - 22]
            continue
        elif x == 29:
            res += [x, x - 1, x - 2, x - 3, x - 4, x - 5, x - 6, x - 7, x - 8, x - 9, x - 10, x - 11, x - 12, x - 13, x - 14, x - 15, x - 16, x - 17, x - 18, x - 19, x - 20, x - 21, x - 22, x - 23, x - 24, x - 25, x - 26, x - 27, x - 28]
            continue
        elif x == 37:
            res += [x, x - 1, x - 2, x - 3, x - 4, x - 5, x - 6, x - 7, x - 8, x - 9, x - 10, x - 11, x - 12, x - 13, x - 14, x - 15, x - 16, x - 17, x - 18, x - 19, x - 20, x - 21, x - 22, x - 23, x - 24, x - 25, x - 26, x - 27, x - 28, x - 29, x - 30, x - 31, x - 32, x - 33, x - 34, x - 35, x - 36]
            continue
        elif x == 41:
            res += [x, x - 1, x - 2, x - 3, x - 4, x - 5, x - 6, x - 7, x - 8, x - 9, x - 10, x - 11, x - 12, x - 13, x - 14, x - 15, x - 16, x - 17, x - 18, x - 19, x - 20, x - 21, x - 22, x - 23, x - 24, x - 25, x - 26, x - 27, x - 28, x - 29, x - 30, x - 31, x - 32, x - 33, x - 34, x - 35, x - 36, x - 37, x - 38, x - 39, x - 40]
            continue
        elif x == 43:
            res += [x, x - 1, x - 2, x - 3, x - 4, x - 5, x - 6, x - 7, x - 8, x - 9, x - 10, x - 11, x - 12, x - 13, x - 14, x - 15, x - 16, x - 17, x - 18, x - 19, x - 20, x - 21, x - 22, x - 23, x - 24, x - 25, x - 26, x - 27, x - 28, x - 29, x - 30, x - 31, x - 32, x - 33, x - 34, x - 35, x - 36, x - 37, x - 38, x - 39, x - 40, x - 41, x - 42]
            continue
        elif x == 47:
            res += [x, x - 1, x - 2, x - 3, x - 4, x - 5, x - 6, x - 7, x - 8, x - 9, x - 10, x - 11, x - 12, x - 13, x -
	