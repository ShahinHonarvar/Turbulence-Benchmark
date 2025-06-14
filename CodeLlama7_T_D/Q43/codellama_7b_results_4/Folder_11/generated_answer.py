 def find_primes_between_indices(my_list):
    # Initialize a list to store the prime numbers
    prime_numbers = []
    # Iterate through the list of integers
    for i in range(55, 77):
        # Check if the number is divisible by any number between 2 and the square root of the number
        for j in range(2, int(i ** 0.5) + 1):
            # If the number is divisible, break out of the loop
            if i % j == 0:
                break

        # If the number is not divisible by any number between 2 and the square root of the number, it is prime
        else:
            prime_numbers.append(i)

    # Return the sorted list of all prime numbers from index 55 to index 76, both inclusive
    return sorted(prime_numbers)
