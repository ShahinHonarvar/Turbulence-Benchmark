
def prime_factors(my_list):
    # Find the prime factorization of the number at index 94
    num = my_list[94]
    factors = set()

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            factors.add(i)

            while num % i == 0:
                num /= i

    factors.add(num)

    return factors
