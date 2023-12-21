def all_right_truncatable_prime(test_tup):
    res = []
    for n in range(2, int(test_tup[85]) + 1):
        if is_prime(n):
            if n % 10 == 0:
                res += [n]
            elif n % 10 == 5:
                res += [n, int(str(n)[0] + '0', 10)]
            elif n % 10 == 7:
                res += [n, int(str(n)[0] + '0', 10), int(str(n)[0] + '5', 10)]
    return res
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    maxDivisor = n**0.5
    i = 5
    while i * i <= maxDivisor:
        if n % i == 0:
            return False
        i += 6
    return True
