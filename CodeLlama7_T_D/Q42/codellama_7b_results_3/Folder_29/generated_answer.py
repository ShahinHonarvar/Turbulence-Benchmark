
def prime_factors(my_list):
    # Find the prime factorization of the number at index 19
    num = my_list[19]
    prime_factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime_factors.add(i)
            while num % i == 0:
                num //= i

    return prime_factors
