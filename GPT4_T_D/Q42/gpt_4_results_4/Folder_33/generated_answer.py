
def prime_factors(int_list):
    number = int_list[321]
    i = 2
    factors = set()
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.add(i)
    if number > 1:
        factors.add(number)
    return factors
