
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    primes = []

    # Iterate through the list from index 28 to index 83
    for i in range(28, 84):
        # Check if the current element is a prime number
        if is_prime(my_list[i]):
            # If it is a prime number, add it to the list of primes
            primes.append(my_list[i])

    # Sort the list of primes in ascending order
    primes.sort()

    # Return the sorted list of primes
    return primes
