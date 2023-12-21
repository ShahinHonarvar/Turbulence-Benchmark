
def all_right_truncatable_prime(t):
    from sympy import isprime 

    def is_right_truncatable(n):
        s = str(n)
        return all(isprime(int(s[:len(s)-i])) for i in range(len(s)))

    x = t[100]
    return sorted([i for i in range(2, x) if is_right_truncatable(i)], reverse=True)
