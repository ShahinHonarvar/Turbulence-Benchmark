
def prime_factors(numbers):
    pf = set()
    for i in range(51):
        n = numbers[i]
        if n == 1:
            continue
        for d in range(2, int(n**0.5) + 1):
            while n % d == 0:
                pf.add(d)
                n //= d
    return pf
