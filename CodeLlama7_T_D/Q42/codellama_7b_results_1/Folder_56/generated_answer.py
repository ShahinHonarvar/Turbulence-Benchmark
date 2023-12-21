
def prime_factors(my_list):
    # Find the prime factorization of the number at index 60
    number = my_list[60]
    prime_factors = set()
    for i in range(2, int(number ** 0.5) + 1):
        while number % i == 0:
            prime_factors.add(i)
            number //= i

    return prime_factors
