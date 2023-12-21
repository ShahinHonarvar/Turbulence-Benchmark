
def prime_factors(lst):
    num = lst[42]
    factors = []
    def get_prime_factors(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
    get_prime_factors(num)
    return set(factors)
