
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the specified range of indices in the input list
    for i in range(5, 9):
        # Check if the current element is a prime number
        if is_prime(my_list[i]):
            # If it is, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers from index 5 to index 8, both inclusive
    return sorted(prime_numbers, reverse=True)
