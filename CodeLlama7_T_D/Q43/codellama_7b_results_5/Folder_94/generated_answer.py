
def find_primes_between_indices(my_list):
    # Define a list to store the prime numbers
    prime_numbers = []

    # Iterate over the list and check if each element is prime
    for i in range(24, 30 + 1):
        # Check if the current number is divisible by any of the first 6 numbers (0 to 6)
        if my_list[i] % my_list[:7].sum() == 0:
            continue

        # If the current number is not divisible by any of the first 6 numbers, it is prime
        else:
            prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers from index 24 to index 30, both inclusive
    return sorted(prime_numbers)
