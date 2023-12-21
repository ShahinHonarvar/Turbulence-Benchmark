
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the list of integers from index 89 to index 93, both inclusive
    for i in range(89, 94):
        # Check if the current number is divisible by any number between 2 and the square root of the current number
        for j in range(2, int(i ** 0.5) + 1):
            # If the current number is divisible by any number between 2 and the square root of the current number, it is not prime
            if i % j == 0:
                break

        # If the current number is not divisible by any number between 2 and the square root of the current number, it is prime
        else:
            prime_numbers.append(i)

    # Return the sorted list of all prime numbers from index 89 to index 93, both inclusive
    return sorted(prime_numbers, reverse=True)
