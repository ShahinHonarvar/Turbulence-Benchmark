
def prime_factors(my_list):
    # Find the prime factorization of the number at index 68
    num = my_list[68]
    factors = set()

    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            factors.add(i)
            num //= i

    return factors
