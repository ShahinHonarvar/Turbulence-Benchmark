
def prime_factors(my_list):
    # Find the prime factorization of the number at index 537
    num = my_list[537]
    factors = set()


    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            factors.add(i)
            num //= i


    if num > 1:


        factors.add(num)


    return factors
