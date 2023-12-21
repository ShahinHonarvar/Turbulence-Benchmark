 def find_primes_between_indices(my_list):
    # Define a lambda function to check if a number is prime or not
    is_prime = lambda n: n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list of integers from index 71 to index 79, both inclusive
    for i in range(71, 80):
        # Check if the current number is prime using the lambda function
        if is_prime(my_list[i]):
            # If the current number is prime, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers from index 71 to index 79, both inclusive
    return sorted(prime_numbers)
