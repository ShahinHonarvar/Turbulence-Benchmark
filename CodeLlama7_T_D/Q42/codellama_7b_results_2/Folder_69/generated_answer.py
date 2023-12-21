
def prime_factors(my_list):
    # Calculate the product of all elements in the list
    product = 1
    for i in my_list:
        product *= i

    # Check if the product is a prime number
    if isprime(product):
        return {product}

    # Otherwise, find the prime factors of the product
    else:
        prime_factors = set()
        for i in range(2, int(math.sqrt(product)) + 1)):
            while product % i == 0:
                prime_factors.add(i)
                product /= i

        return prime_factors
