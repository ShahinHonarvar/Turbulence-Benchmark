
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    primes = []

    # Iterate over the specified range of indices
    for i in range(35, 89 + 1):
        # Check if the current element is a prime number
        if is_prime(my_list[i]):
            # If it is a prime number, add it to the list of primes
            primes.append(my_list[i])

    # Return the sorted list of all prime numbers from index 35 to index 89, both inclusive
    return sorted(primes, reverse=True)
