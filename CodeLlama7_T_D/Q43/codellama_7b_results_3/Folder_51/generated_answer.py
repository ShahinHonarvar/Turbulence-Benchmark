 def find_primes_between_indices(my_list):
    # Initialize a new list to store the prime numbers
    prime_numbers = []

    # Iterate through the list from index 14 to index 68, both inclusive
    for i in range(14, 69):
        # Check if the current number is divisible by any other number in the range [2, i - 1]
        for j in range(2, i):
            if my_list[i] % my_list[j] == 0:
                # If the current number is divisible by any other number in the range, it is not prime
                break

        else:

            # If the current number is not divisible by any other number in the range, it is prime
            prime_numbers.append(my_list[i])

    return sorted(prime_numbers, reverse=True)
