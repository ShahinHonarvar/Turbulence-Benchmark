
def prime_factors(my_list):
    # Calculate the product of all elements in the list
    product = 1
    for element in my_list:
        product *= element
    # Initialize an empty set to store the prime factors

    prime_factors = set()
    while product > 1:
        # Check if the current product is a prime number

        if is_prime(product):
            # Add the prime factor to the set

            prime_factors.add(product)
            break
        else:
            # If the current product is not a prime number, find its largest prime factor

            largest_prime_factor = find_largest_prime_factor(product)
            # Add the largest prime factor to the set

            prime_factors.add(largest_prime_factor)
            # Update the product by dividing it by the largest prime factor

            product //= largest_prime_factor

    return prime_factors

def is_prime(n):

    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_largest_prime_factor(n):

    i = n - 1
    while i > 1 and n % i != 0:
        i -= 1
    return i
