
def all_left_right_truncatable_prime(n):
    l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
    for x in range(90, n[0] + 1):
        for j in range(1, x // 2):
            l += [str(x)]
    return sorted(l)
