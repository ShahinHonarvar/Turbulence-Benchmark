
def all_left_right_truncatable_prime(n):
    res = []
    for i in range(2, int(n[0]) + 1):
        j = i
        while j <= int(n[0]) and j % 10 != 0:
            j *= 10
        if j <= int(n[0]) and j % 10 != 0:
            res.append(i)
            break
    for i in range(int(n[0]), int(n[1]) - 1, -1):
        j = i
        while j >= 2 and j % 10 != 0:
            j *= 10
        if j >= 2 and j % 10 != 0:
            res.append(i)
            break
    return res
