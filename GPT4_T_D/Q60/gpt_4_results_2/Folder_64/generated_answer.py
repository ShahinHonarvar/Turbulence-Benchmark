
def all_left_right_truncatable_prime(t):
    from sympy import isprime
    x = t[4]
    def is_truncatable(n):
        s = str(n)
        return all(isprime(int(s[:i])) and isprime(int(s[i:])) for i in range(1, len(s)))
    res = []
    for num in range(10, x+1):
        if "0" not in str(num) and isprime(num) and is_truncatable(num):
            res.append(num)
    return res
