
def all_left_right_truncatable_prime(t):
    from sympy import isprime
    x = t[96]
    results = []

    def is_truncatable(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(0, len(n)):
            if not isprime(int(n[i:])) or not isprime(int(n[:len(n)-i])):
                return False
        return True

    for i in range(10, x+1):
        if is_truncatable(i):
            results.append(i)
    return sorted(results, reverse=True)
