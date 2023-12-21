
def all_left_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the tuple elements and check if each element is a prime number
    for i in range(len(tuple)):
        element = tuple[i]
        if is_prime(element):
            prime_numbers.append(element)

    # Sort the list of prime numbers in ascending order
    sorted_prime_numbers = sorted(prime_numbers)

    return sorted_prime_numbers
