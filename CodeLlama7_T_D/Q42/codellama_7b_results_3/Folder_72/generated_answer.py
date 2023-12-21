
def prime_factors(my_list):
    # Calculate the product of all elements in the list
    product = 1
    for i in my_list:
        product *= i

    # Find the prime factors by dividing the product by successive divisors

    factors = set()

    for i in range(2, int(product ** 0.5) + 1):
        while product % i == 0:
            factors.add(i)
            product /= i

    return factors
