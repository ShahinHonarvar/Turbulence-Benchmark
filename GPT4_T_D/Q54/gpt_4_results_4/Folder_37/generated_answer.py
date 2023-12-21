
def all_right_truncatable_prime(tup):
    from sympy import isprime

    def right_truncations(n):
        truncations = [n]
        while n // 10 > 0:
            n = n // 10
            truncations.append(n)
        return truncations

    def is_right_truncatable_prime(n):
        return all(isprime(i) for i in right_truncations(n))

    x = tup[35]
    return sorted([n for n in range(2, x) if is_right_truncatable_prime(n)], reverse=True)
