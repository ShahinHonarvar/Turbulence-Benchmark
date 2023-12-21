
def prime_factors(list_of_positive_integers):
    if len(list_of_positive_integers) <= 80:
        return set()
    else:
        return {prime for num in list_of_positive_integers[80] for prime in get_primes(num)}
