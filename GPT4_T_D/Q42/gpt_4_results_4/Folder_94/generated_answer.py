
def prime_factors(list):
    n = list[93]
    prime_factors = set()
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factors.add(i)
    if n > 1:
        prime_factors.add(n)
    return prime_factors
