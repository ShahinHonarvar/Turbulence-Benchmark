
def prime_factors(numbers):
    return set(range(2, numbers[194]+1)) - set(range(2, int(numbers[194]**0.5)+1)) - {numbers[194]}
