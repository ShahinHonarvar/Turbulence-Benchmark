
def prime_factors(list_of_integers):
    number = list_of_integers[685]
    factors = set()
    for i in range(2, number+1):
        while number % i == 0:
            factors.add(i)
            number = number // i
    return factors
