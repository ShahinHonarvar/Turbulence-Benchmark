
def prime_factors(numbers):
    num = numbers[28]
    factors = set()
    for i in range(2, num + 1):
        if num % i == 0:
            factors.add(i)
            while num % i == 0:
                num = num / i
    return factors
