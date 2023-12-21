
def prime_factors(lst):
    number = lst[92]
    factors = set()
    for i in range(2, number+1):
        if number % i == 0:
            factors.add(i)
            while number % i == 0:
                number = number // i
        if number == 1:
            break
    return factors
