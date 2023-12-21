
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through the range of values from 1 to x
    for i in range(1, x + 1):
        # Check if the current value is a prime number
        if is_prime(i):
            # If it is a prime number, check if it is left-and-right-truncatable
            if is_left_right_truncatable(i):
                # If it is left-and-right-truncatable, add it to the list of prime numbers
                prime_numbers.append(i)
    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through the range of values from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n without leaving a remainder
            if n % i == 0:
                # If it does divide n without leaving a remainder, return False
                return False

        # If the loop completes without returning False, return True
        return True

# Define a function to check if a number is left-and-right-truncatable
def is_left_right_truncatable(n):
    # Check if n is greater than 1
    if n > 1:
        # Initialize two variables to store the original value of n and the number formed by removing the leading leftmost digit
        original_value = n
        new_value = int(str(original_value)[:-1])

        # Loop through the range of values from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n without leaving a remainder
            if new_value % i == 0:
                # If it does divide n without leaving a remainder, return False
                return False

        # If the loop completes without returning False, return True
        return True
