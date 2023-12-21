def all_right_truncatable_prime(test_tup):
    res = []
    for x in range(int(test_tup[0]), int(test_tup[1]) + 1):
        if x % 2 == 0:
            continue
        for d in range(2, int(str(x)[-1]) + 1):
            if str(x)[-1] % d == 0:
                break
            elif is_prime(x // 10**(d - 1)):
                res.append(x // 10**(d - 1))
    return res
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    maxDivisor = int(n ** .5)
    if n % 2 == 0 or n % 3 == 0:
        maxDivisor = int(n ** .5) - 1
    for d in range(5, maxDivisor + 1):
        if n % d == 0:
            return False
    return True
