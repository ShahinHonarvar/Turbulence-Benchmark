
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the results
    result = []

    # Iterate from 2 to x, inclusive
    for i in range(2, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):

                # Add i to the result list
                result.append(i)

    # Sort the result list in descending order
    result.sort(reverse=True)

    # Return the result list
    return result

# Check if a number is prime
def is_prime(n):

    # If n is less than 2, it is not prime
    if n < 2:
        return False

    # If any number between 2 and sqrt(n) divides n, it is not prime
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If no number between 2 and sqrt(n) divides n, it is prime
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):

    # If n contains 0, it is not left-and-right-truncatable prime number
    if '0' in str(n):
        return False

    # Remove the leading leftmost and last rightmost digits from n
    left = int(str(n)[:2])
    right = int(str(n)[-2:]))

    # Check if the resulting number is prime
    if is_prime(left) and is_prime(right):
        return True

    # If either of the resulting numbers is not prime, it is not left-and-right-truncatable prime number
    else:
        return False
