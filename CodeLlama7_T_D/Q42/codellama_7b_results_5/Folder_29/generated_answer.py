
def prime_factors(my_list):
    # Check if input is a list
    if not isinstance(my_list, list):
        raise ValueError("Input must be a list")
    # Get the integer at index 19
    num = my_list[19]
    # Initialize an empty set to store prime factors
    prime_factors = set()
    # Iterate through all numbers less than or equal to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        # Check if i is a factor of num
        if num % i == 0:
            # Add i as a prime factor
            prime_factors.add(i)
            # If i is a prime number, add it to the set of prime factors
            if is_prime(i):
                prime_factors.add(i)
    return prime_factors

def is_prime(n):
    # Check if n is an integer greater than 1
    if not isinstance(n, int) or n < 2:
        raise ValueError("Input must be a positive integer")
    # Iterate from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # If n is divisible by i, it is not prime
        if n % i == 0:
            return False
