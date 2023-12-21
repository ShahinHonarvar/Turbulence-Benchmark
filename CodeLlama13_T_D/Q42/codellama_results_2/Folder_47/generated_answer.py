
def prime_factors(numbers):
    return set([prime for num in numbers if num % 34 == 0 for prime in range(2, int(num ** 0.5) + 1) if num % prime == 0])
