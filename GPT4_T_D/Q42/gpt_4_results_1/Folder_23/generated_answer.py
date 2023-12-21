
def prime_factors(numbers):
    number = numbers[69]
    primes = []
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            primes.append(i)
    if number > 1:
        primes.append(number)
    return set(primes)
