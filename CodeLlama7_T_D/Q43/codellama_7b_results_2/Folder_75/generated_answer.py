
def find_primes_between_indices(my_list):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the list of integers from index 46 to index 61, both inclusive
    for i in range(46, 62):
        # Check if the current element is a prime number
        if is_prime(my_list[i]):
            # If it is a prime number, add it to the list of prime numbers
            prime_numbers.append(my_list[i])

    # Return the sorted list of all prime numbers from index 46 to index 61, both inclusive
    return sorted(prime_numbers)

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If the remainder of dividing n by i is zero, then n is not prime
            if n % i == 0:
                return False

    # If n is greater than 1 and it is divisible only by 1 and itself, then it is prime
    return True
