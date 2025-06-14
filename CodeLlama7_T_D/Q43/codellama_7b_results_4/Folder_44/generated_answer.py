
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate through the list starting from index 19
    for i in range(19, len(my_list)):
        # Check if the current number is prime
        if is_prime(my_list[i]):
            # If it is prime, add it to the list of prime numbers
            prime_numbers.append(my_list[i])
    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)
    return prime_numbers
