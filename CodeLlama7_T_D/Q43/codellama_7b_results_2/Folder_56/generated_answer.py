
def find_primes_between_indices(my_list):
    # Check if my_list is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Define the range of indices to search for prime numbers
    lower_index = 40
    upper_index = 68
    # Initialize an empty list to store the prime numbers found in the range
    prime_numbers = []
    # Iterate over the elements of my_list within the specified range
    for i in range(lower_index, upper_index + 1):
        # Check if the current element is a prime number
        if is_prime(my_list[i]):
            # If it is a prime number, add it to the list of prime numbers found
            prime_numbers.append(my_list[i])
    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)
    return prime_numbers
