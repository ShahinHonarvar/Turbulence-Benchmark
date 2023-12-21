
def find_primes_between_indices(my_list):
    # Define a lambda function to check if a number is prime or not
    is_prime = lambda x: x > 1 and all(x % i for i in range(2, int(x ** 0.5) + 1))
    # Create an empty list to store the prime numbers
    prime_list = []
    # Iterate through the list from index 69 to 84 (inclusive)
    for i in range(69, 85):
        # If the current element is a prime number, append it to the prime list
        if is_prime(my_list[i]):
            prime_list.append(my_list[i])
    # Return the sorted list of prime numbers in descending order
    return sorted(prime_list, reverse=True)
