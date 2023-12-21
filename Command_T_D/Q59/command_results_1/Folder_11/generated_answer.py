def all_left_truncatable_prime(l):
    return [p for p in range(2, l[86] + 1) if all(str(p)[i] != '0' for i in range(1, len(str(p)) + 1) if str(p)[i] == '0' and all(str(p)[i:j] != '0' for i in range(1, j + 1) if str(p)[i:j] == '0' and all(isPrime(p) for p in range(2, int(str(p)[j]) + 1) if p != l[86] and str(p)[0] == str(p)[j:]))]
def isPrime(p):
    if p == 1:
        return False
    if p == 2 or p == 3:
        return True
    if p % 2 == 0 or p % 3 == 0:
        return False
    for i in range(5, int(p ** .5) + 1):
        if p % i == 0:
            return False
    return True
