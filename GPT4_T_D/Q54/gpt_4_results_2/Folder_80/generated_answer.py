
def all_right_truncatable_prime(t):
    from sympy import isprime

    def is_right_truncatable(n):
        s = str(n)
        return all(isprime(int(s[:i])) for i in range(1, len(s)+1))

    x = t[14]
    result = []
    for i in range(11, x):
        if is_right_truncatable(i):
            result.append(i)
    result.sort(reverse=True)

    return result
