 def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the results
    results = []

    # Loop through the numbers from 1 to x, inclusive
    for num in range(1, x + 1):

        # Check if the number is a prime number
        if is_prime(num):

            # Check if the number is left-and-right-truncatable prime
            if is_left_right_truncatable_prime(num):

                # Add the number to the results list
                results.append(num)

    # Sort the results list in descending order
    results.sort(reverse=True)

    # Return the sorted results list
    return results

# Check if a number is prime
def is_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If the number is greater than 1 and it is not divisible by any number between 2 and n - 1, it is prime
    return True

# Check if a number is left-and-right-truncatable prime
def is_left_right_truncatable_prime(n):

    # Check if the number is not prime
    if not is_prime(n):
        return False

    # Check if the number contains a 0 digit
    if '0' in str(n):
        return False

    # Remove the leading leftmost and last rightmost digits of the number
    leading_leftmost = int(str(n)[:2])
    last_rightmost = int(str(n)[-2:]))

    # Check if the number is still prime after removing the leading leftmost and last rightmost digits
    if not is_prime(leading_leftmost) or not is_prime(last_rightmost):
        return False

    # If the number is a prime number that contains no 0 and remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime, it is a left-and-right-truncatable prime
    return True
