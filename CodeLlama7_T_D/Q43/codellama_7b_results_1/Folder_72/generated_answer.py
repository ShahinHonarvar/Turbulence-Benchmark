 def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list from index 39 to index 51, both inclusive
    for i in range(39, 52):
        # Check if the current number is a prime number using the Sieve of Eratosthenes algorithm
        if my_list[i] > 1:
            for j in range(2, my_list[i]):
                if my_list[i] % j == 0:
                    break

            else:

                # If the current number is a prime number, add it to the list of prime numbers
                prime_numbers.append(my_list[i])

    return sorted(prime_numbers)
