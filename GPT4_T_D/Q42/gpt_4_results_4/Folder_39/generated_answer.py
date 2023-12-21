
def prime_factors(numbers):
    num = numbers[59]
    factors = []
    for i in range(2, num + 1):
        while num % i == 0:
            factors.append(i)
            num = num / i
    return set(factors)
