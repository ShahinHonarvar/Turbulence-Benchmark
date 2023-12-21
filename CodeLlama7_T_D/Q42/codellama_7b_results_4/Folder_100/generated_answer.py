
def prime_factors(my_list):
    # Calculate the product of all elements in the list
    product = 1
    for element in my_list:
        product *= element
    # Initialize an empty set to store the prime factors

    prime_factors = set()
    # Loop through the range of numbers from 2 to the square root of the product

    for i in range(2, int(product ** 0.5) + 1):
        # If the number is a factor of the product, add it to the set of prime factors

        if product % i == 0:
            prime_factors.add(i)
    return prime_factors
