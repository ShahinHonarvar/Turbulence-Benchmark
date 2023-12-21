 def find_primes_between_indices(my_list):
    # Initialize an empty list to store prime numbers
    prime_numbers = []

    # Loop through the list of integers from index 261 to 459, both inclusive
    for i in range(261, 459 + 1):
        # Check if the current number is a prime number
        if my_list[i] > 1:
            # Loop through the list of integers from index 2 to the current number
            for j in range(2, my_list[i] + 1):
                # Check if the current number is divisible by any number other than 1 and itself
                if my_list[i] % j == 0:
                    # If the current number is divisible by any number other than 1 and itself, break out of the loop
                    break

            # If the current number is not divisible by any number other than 1 and itself, add it to the list of prime numbers
            else:
                prime_numbers.append(my_list[i])

    # Sort the list of prime numbers in ascending order
    prime_numbers.sort()

    # Return the sorted list of all prime numbers from index 261 to index 459, both inclusive
    return prime_numbers
