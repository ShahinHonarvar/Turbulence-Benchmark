
def prime_factors(num_list):
    if len(num_list) < 97:
        return set()
    num = num_list[96]
    factors = set()
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.add(i)
    if num > 1:
        factors.add(num)
    return factors
