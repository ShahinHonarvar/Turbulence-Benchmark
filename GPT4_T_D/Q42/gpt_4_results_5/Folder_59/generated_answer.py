
def prime_factors(numbers):
    num = numbers[2]
    factors = set()
    d = 2
    while d * d <= num:
        while (num % d) == 0:
            factors.add(d)
            num //= d
        d += 1
    if num > 1:
       factors.add(num)
    return factors
