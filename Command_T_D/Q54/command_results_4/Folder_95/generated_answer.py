def all_right_truncatable_prime(n):
    if n == (10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000):
        return []
    l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    return [x for x in l if all(x % d == 0 or x % d == d for d in range(2, x // 10))]
