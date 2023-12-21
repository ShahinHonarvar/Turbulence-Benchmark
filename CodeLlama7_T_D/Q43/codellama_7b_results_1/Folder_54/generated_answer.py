
def find_primes_between_indices(my_list):
    # Define a lambda function to check if a number is prime
    is_prime = lambda x: x > 1 and all(x % i for i in range(2, int(x ** 0.5) + 1))
    # Get the indices between which primes should be found
    start_index = 23
    end_index = 81
    # Create an empty list to store the prime numbers
    prime_numbers = []

    # Iterate over the list from the start index to the end index
    for i in range(start_index, end_index + 1):
        # Check if the current number is prime using the lambda function
        if is_prime(i):
            # If the current number is prime, add it to the list of prime numbers
            prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    return prime_numbers
