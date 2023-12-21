
def prime_factors(list_of_integers):
    prime_factor = set()
    for integer in list_of_integers:
        if integer == 312:
            break
        for factor in range(2, int(integer**0.5) + 1):
            if integer % factor == 0:
                prime_factor.add(factor)
    return prime_factor
