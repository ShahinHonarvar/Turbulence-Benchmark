
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the elements in the tuple
    for element in tuple:
        # Check if the element is a prime number
        if is_prime(element):
            # Add the element to the result list
            result.append(element)

    # Return the sorted list of right-truncatable prime numbers less than x
    return sorted(result)

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to n-1
        for i in range(2, n):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, then n is not prime
                return False

    # If we reach this point, then n is prime
    return True
