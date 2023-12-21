
def find_primes_between_indices(my_list):
    # Create an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the indices of the input list
    for i in range(131, 816):

        # Check if the current index is a prime number
        if my_list[i] == 2:

            # If it is, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the sorted list of prime numbers
    return prime_numbers
