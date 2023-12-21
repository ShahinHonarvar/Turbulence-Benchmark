
def find_primes_between_indices(my_list):
    # Initialize variables
    prime_numbers = []
    start_index = 167
    end_index = 785
    # Iterate through the list and check for prime numbers
    for i in range(start_index, end_index + 1):
        is_prime = True
        for j in range(2, my_list[i]):
            if my_list[i] % j == 0:
                is_prime = False
                break

        # If the number is prime, add it to the list
        if is_prime:
            prime_numbers.append(my_list[i])

    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)
