
def find_primes_between_indices(my_list):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Iterate through the list from index 66 to index 81, both inclusive
    for i in range(66, 82):
        # Check if the current element is divisible by any number between 2 and the square root of the current element
        for j in range(2, int(my_list[i] ** 0.5) + 1)):
            if my_list[i] % j == 0:
                # If it is divisible, break out of the inner loop and move on to the next element
                break

        else:

            # If the current element is not divisible by any number between 2 and the square root of the current element, it is prime
            prime_numbers.append(my_list[i])

    # Return the sorted list of prime numbers in ascending order
    return sorted(prime_numbers)
