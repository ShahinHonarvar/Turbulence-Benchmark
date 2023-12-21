
def prime_factors(my_list):
    # Find the factorization of the number at index 276
    num = my_list[276]
    factors = []

    for i in range(1, int(num ** 0.5) + 1):

        if num % i == 0:

            factors.append(i)


            if num / i != i:

                factors.append(num // i)


    return set(factors)
