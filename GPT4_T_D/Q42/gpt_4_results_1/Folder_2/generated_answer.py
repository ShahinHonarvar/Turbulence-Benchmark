
def prime_factors(integer_list):
    num = integer_list[702]
    factors = set()
    divisor = 2
    while divisor <= num:
        if num % divisor == 0:
            factors.add(divisor)
            num = num / divisor
        else:
            divisor += 1
    return factors
