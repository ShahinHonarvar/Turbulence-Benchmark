
def find_primes_between_indices(my_list):
    # Create a copy of the original list
    prime_list = my_list[:]
    # Initialize a flag variable
    is_prime = True

    for i in range(773, 805 + 1):
        # Check if the current number is divisible by any number between 2 and the square root of the current number
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        # If the current number is prime, add it to the prime list
        if is_prime:
            prime_list.append(i)

    # Return the sorted list of all prime numbers from index 773 to index 805, both inclusive
    return sorted(prime_list)
