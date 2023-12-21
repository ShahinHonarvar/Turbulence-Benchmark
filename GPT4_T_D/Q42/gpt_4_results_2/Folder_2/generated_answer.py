
def prime_factors(lst):
    if len(lst) <= 702:
        return "Error: Index out of range"
    n = lst[702]
    factors = set()
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors
