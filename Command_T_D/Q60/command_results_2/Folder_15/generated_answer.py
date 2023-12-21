
def all_left_right_truncatable_prime(x):
    return sorted((p for p in range(2, x+1) if all(int(c) for c in str(p)) and p not in [2, 3, 5, 7, 11, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 99999, 99667, 99883, 99937])
