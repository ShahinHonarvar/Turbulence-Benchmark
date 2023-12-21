
def all_left_truncatable_prime(tuple):
    # Initialize the list of left-truncatable prime numbers
    left_truncatable_primes = []
    # Get the integer at index 0 of the tuple
    x = tuple[0]
    # Loop through all numbers less than x
    for i in range(2, x):
        # Check if i is a prime number
        if is_prime(i):
            # Check if the leading leftmost digit of i is successively removed, then all resulting numbers are prime
            if all_prime(i):
                # Add i to the list of left-truncatable prime numbers
                left_truncatable_primes.append(i)
    # Return the list of left-truncatable prime numbers sorted in descending order
    return sorted(left_truncatable_primes, reverse=True)
# Function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all numbers less than or equal to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # If the loop completes successfully, return True
    return True

# Function to check if a number is prime after successively removing leading leftmost digits
def all_prime(n):
    # Initialize the list of numbers obtained by successively removing leading leftmost digits from n
    numbers = []

    # Loop through all numbers less than or equal to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i divides n
        if n % i == 0:
            # Add the number obtained by removing leading leftmost digits from n divided by i to the list of numbers
            numbers.append(n // i)
    # Return True if all numbers in the list are prime, False otherwise
    return all(is_prime(num) for num in numbers))```
