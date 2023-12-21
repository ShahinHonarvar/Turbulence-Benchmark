
def all_left_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []
    
    # Iterate through the numbers from 1 to x
    for i in range(1, x + 1):
        # If the current number is a prime number and it is left-truncatable prime number, then add it to the list of prime numbers
        if is_prime(i) and is_left_truncatable_prime(i):
            prime_numbers.append(i)
    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)
    # Return the list of prime numbers
    return prime_numbers
