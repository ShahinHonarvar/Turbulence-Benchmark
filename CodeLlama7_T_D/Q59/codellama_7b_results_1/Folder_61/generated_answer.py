
def all_left_truncatable_prime(x):
    # Initialize an empty list to store the results
    results = []

    # Iterate from 2 to x
    for i in range(2, x + 1):
        # If i is a prime number and it is left-truncatable prime number, add it to the result list
        if is_prime(i) and is_left_truncatable_prime(i):
            results.append(i)

    # Return the sorted result list in descending order
    return sorted(results, reverse=True)

# Function to check if a number is prime or not
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Check if n is a multiple of 2 to 10
        for i in range(2, 11):
            if n % i == 0:
                return False

        # If n is a prime number, return True
        return True

# Function to check if a number is left-truncatable prime or not
def is_left_truncatable_prime(n):
    # Check if n is a prime number and it contains no 0
    if is_prime(n) and '0' not in str(n):
        # Remove the leading leftmost digit of the number
        removed = int(str(n)[1:])

        # If the resulting number is a prime number, return True
        if is_prime(removed):
            return True

    # If the number is not a prime number or it contains 0, return False
    return False
