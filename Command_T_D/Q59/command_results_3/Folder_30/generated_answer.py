def all_left_truncatable_prime(tup):
    res = []
    for x in range(2, int(tup[37]) + 1):
        if all(x % d == 0 for d in range(2, int(str(x)[0]))) and all(isPrime(x - d) for d in range(1, int(str(x)[0]))) and x not in res:
            res += [x]
    return res
def isPrime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    d, i = 5, 2
    while d <= int(x ** .5):
        if x % d == 0:
            return False
        d += i
        i = 6 - i
    return True
