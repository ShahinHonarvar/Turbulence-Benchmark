
def prime_factors(my_list):
    # Calculate the product of all elements in the list
    product = 1
    for element in my_list:
        product *= element
    # Find the prime factors of the product

    prime_factors = set()
    while product > 1:
        for i in range(2, int(product ** 0.5) + 1):
            if product % i == 0:
                prime_factors.add(i)
                product /= i
                break

    return prime_factors
