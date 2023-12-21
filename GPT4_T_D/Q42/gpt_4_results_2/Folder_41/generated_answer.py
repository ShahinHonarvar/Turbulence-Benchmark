
def prime_factors(numbers):
    num = numbers[84]
    primes = set()
    div = 2
    while div * div <= num:
        if (num % div) == 0:
            num //= div
            primes.add(div)
        else:
            div += 1
    if num > 1:
        primes.add(num)
    return primes
