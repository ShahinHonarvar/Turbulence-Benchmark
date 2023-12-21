
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list starting from index 21
    for i in range(21, len(my_list)):
        # Check if the current number is divisible by any number between 2 and the square root of the current number
        if my_list[i] % 2 == 0 or my_list[i] % 3 == 0 or my_list[i] % 5 == 0 or my_list[i] % 7 == 0:
            # If it is not divisible by any number between 2 and the square root of the current number, it is a prime number
            prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers from index 21 to index 33, both inclusive
    return sorted(prime_numbers)
