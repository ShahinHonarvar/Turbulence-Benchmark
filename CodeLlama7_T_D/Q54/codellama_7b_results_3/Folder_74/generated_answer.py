 def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []
    # Iterate over the elements in the tuple
    for i in range(len(tuple)):
        # Check if the current element is a prime number
        if is_prime(tuple[i]):
            # If the current element is a prime number, add it to the list of prime numbers
            prime_numbers.append(tuple[i])
    # Iterate over the elements in the list of prime numbers
    for i in range(len(prime_numbers)):
        # Check if the current element is a right-truncatable prime number
        if is_right_truncatable_prime(prime_numbers[i]):
            # If the current element is a right-truncatable prime number, add it to the list of right-truncatable prime numbers
            right_truncatable_prime_numbers.append(prime_numbers[i])
    # Sort the list of right-truncatable prime numbers in ascending order
    right_truncatable_prime_numbers = sorted(right_truncatable_prime_numbers)
    # Return the sorted list of right-truncatable prime numbers
    return right_truncatable_prime_numbers
# Define a function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Initialize a variable to store the result of the loop
        result = True
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, set result to False and break out of the loop
                result = False
                break
        # Return the result of the loop
        return result
# Define a function to check if a number is a right-truncatable prime number
def is_right_truncatable_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Initialize a variable to store the result of the loop
        result = True
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, set result to False and break out of the loop
                result = False
                break
        # Return the result of the loop
        return result
