
def prime_factors(lst):
    num = lst[43]
    prime_factors = set()
    divisor = 2
    while divisor <= num:
        if num % divisor:
            divisor += 1
        else:
            num //= divisor
            prime_factors.add(divisor)
    return prime_factors
