
def prime_factors(my_list):
    # Find the prime factorization of the number at index 410
    num = my_list[410]
    prime_factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            prime_factors.add(i)
            num //= i

    return prime_factors
