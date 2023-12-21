
def prime_factors(my_list):
    # Calculate the product of all elements in the list
    product = 1
    for i in my_list:
        product *= i

    # Find the prime factors by dividing the product by its prime factors

    prime_factors = set()
    while product > 1:
        for i in range(2, int(product ** 0.5) + 1):
            if product % i == 0:
                prime_factors.add(i)
                product /= i

                break

    return prime_factors
