 def find_primes_between_indices(my_list):
    # Initialize variables
    prime_numbers = []
    start_index = 16
    end_index = 25
    # Iterate over the list in the specified range
    for i in range(start_index, end_index + 1):
        # Check if the current number is prime
        is_prime = True
        for j in range(2, int(my_list[i]) ** 0.5 + 1):
            if my_list[i] % j == 0:
                is_prime = False
                break

        # If the current number is prime, add it to the list of prime numbers
        if is_prime:
            prime_numbers.append(my_list[i])

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    return prime_numbers
