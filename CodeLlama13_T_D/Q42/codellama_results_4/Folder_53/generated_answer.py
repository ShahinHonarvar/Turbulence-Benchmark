
def prime_factors(lst):
    return set([factor for num in lst if isinstance(num, int) and num > 1 for factor in range(2, int(num**0.5) + 1) if num % factor == 0])
