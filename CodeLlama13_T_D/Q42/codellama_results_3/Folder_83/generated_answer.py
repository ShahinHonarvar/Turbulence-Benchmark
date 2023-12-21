
def prime_factors(integers):
    return {factor for factor in range(2, integers[95]) if integers[95] % factor == 0 and is_prime(factor)}
