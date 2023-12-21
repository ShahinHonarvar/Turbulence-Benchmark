
def prime_factors(integers):
    return set([factor for i in range(len(integers)) if integers[i] == 37 for factor in get_prime_factors(integers[i])])

def get_prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return set(factors)
