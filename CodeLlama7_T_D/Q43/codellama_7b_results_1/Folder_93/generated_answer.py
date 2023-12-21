
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the list from index 76 to index 95, both inclusive
    for i in range(76, 96):
        # Check if the current element is a prime number
        if is_prime(my_list[i]):
            # If it is a prime number, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers from index 76 to index 95, both inclusive
    return sorted(prime_numbers)
