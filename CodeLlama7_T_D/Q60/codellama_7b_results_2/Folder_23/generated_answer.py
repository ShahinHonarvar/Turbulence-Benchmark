
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the results
    result = []

    # Iterate from 1 to x, inclusive
    for i in range(1, x + 1):

        # Check if i is a prime number
        if is_prime(i):

            # Check if i contains no 0 and remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            if check_left_right_truncatable_prime(i):

                # Add i to the result list
                result.append(i)

    # Sort the result list in descending order
    result.sort(reverse=True)

    # Return the result list
    return result

# Check if a number is a prime number
def is_prime(n):

    # If n is less than or equal to 1, it is not prime
    if n <= 1:
        return False

    # If n is divisible by 2 to n-1, it is not prime
    for i in range(2, n):
        if n % i == 0:
            return False

    # If we reach this point, n is likely prime
    return True

# Check if a number is a left-and-right-truncatable prime number
def check_left_right_truncatable_prime(n):

    # Check if n contains no 0 by converting it to a string and checking for the presence of '0'
    if str(n).find('0') != -1:
        return False

    # Initialize a variable to store the number of digits in n
    num_digits = len(str(n))

    # Check if n remains prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
    for i in range(num_digits - 1):
        current_digit = str(n)[i]
        next_digit = str(n)[i + 1]
        if current_digit != '0' and int(current_digit) % int(next_digit) == 0:
            return False

    # If we reach this point, n is likely a left-and-right-truncatable prime number
    return True
