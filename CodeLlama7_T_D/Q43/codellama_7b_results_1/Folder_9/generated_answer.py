
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the indices of the list
    for i in range(23, 40):
        # Check if the current number is divisible by any number between 2 and the square root of the number
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break

        # If the current number is prime, add it to the list of prime numbers
        else:
            prime_numbers.append(i)

    # Return the sorted list of all prime numbers from index 23 to index 39, both inclusive
    return sorted(prime_numbers)
