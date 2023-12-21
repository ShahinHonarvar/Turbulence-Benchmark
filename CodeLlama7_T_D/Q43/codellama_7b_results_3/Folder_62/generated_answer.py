
def find_primes_between_indices(my_list):
    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Loop through all the numbers in the list
    for i in range(29, 98):
        # Check if the number is divisible by any of the first 10 prime numbers
        is_prime = True
        for j in range(2, 11):
            if my_list[i] % my_list[j] == 0:
                is_prime = False
                break

        # If the number is prime, add it to the list of prime numbers
        if is_prime:
            prime_numbers.append(my_list[i])

    # Return the sorted list of prime numbers in descending order
    return sorted(prime_numbers, reverse=True)
