
def prime_factors(numbers):
    return set([factor for factor in range(2, int(math.sqrt(numbers[132])) + 1) if numbers[132] % factor == 0 and is_prime(factor)])
