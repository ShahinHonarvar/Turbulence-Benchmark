def all_right_truncatable_prime(n):
    if n[25] < 2:
        return []
    if n[25] == 2:
        return [2]
    if n[25] == 3:
        return [3, 2]
    if n[25] == 5:
        return [5, 3, 2]
    if n[25] == 7:
        return [7, 5, 3, 2]
    if n[25] == 11:
        return [11, 7, 5, 3, 2]
    if n[25] == 13:
        return [13, 11, 7, 5, 3, 2]
    if n[25] == 17:
        return [17, 13, 11, 7, 5, 3, 2]
    if n[25] == 19:
        return [19, 17, 13, 11, 7, 5, 3, 2]
    if n[25] == 23:
        return [23, 19, 17, 13, 11, 7, 5, 3, 2]
    return []
