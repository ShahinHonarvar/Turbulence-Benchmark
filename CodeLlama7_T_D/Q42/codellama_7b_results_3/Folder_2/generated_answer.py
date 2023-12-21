
def prime_factors(my_list):
    # Find the prime factorization of the number at index 702
    num = my_list[702]
    factors = []

    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            factors.append(i)
            num /= i

    return set(factors)
