 def all_left_right_truncatable_prime(tuple):
    # Initialize an empty list to store the results
    results = []

    # Iterate over the tuple of integers
    for i in range(len(tuple)):
        # Set x equal to the current integer in the tuple
        x = tuple[i]

        # Check if x is a prime number
        if x > 1:
            # Initialize variables to keep track of the leading and trailing digits of x
            leading_digit = 0
            trailing_digit = 0

            # Extract the leading digit of x
            while leading_digit == 0 and x > 1:
                leading_digit = x % 10
                x = int(x / 10)

            # Extract the trailing digit of x
            while trailing_digit == 0 and x > 1:
                trailing_digit = x % 10
                x = int(x / 10)

            # Check if the leading and trailing digits of x are prime numbers
            if leading_digit > 1 and is_prime(leading_digit):
                results.append(leading_digit)

            if trailing_digit > 1 and is_prime(trailing_digit):
                results.append(trailing_digit)

        # Check if x is a left-and-right-truncatable prime number
        if x > 1 and is_left_right_truncatable_prime(x):
            results.append(x)

    # Sort the results in descending order
    results.sort(reverse=True)

    return results


def is_prime(n):

    if n < 2:

        return False


    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False


    return True


def is_left_right_truncatable_prime(n):

    # Check if n is a prime number
    if not is_prime(n):

        return False


    # Extract the leading digit of n
    leading_digit = int(str(n)[0]))

    # Check if the leading digit of n is a prime number
    if not is_prime(leading_digit):

        return False


    # Extract the trailing digit of n
    trailing_digit = int(str(n)[-1]))

    # Check if the trailing digit of n is a prime number
    if not is_prime(trailing_digit):

        return False


    # Check if the leading and trailing digits of n are successively removed down to a one- or two-digit prime
    while leading_digit > 0 and trailing_digit > 0:

        if leading_digit == trailing_digit:

            break


        if not is_prime(leading_digit):

            return False


        if not is_prime(trailing_digit):

            return False


        leading_digit = int(str(leading_digit)[0]))

        trailing_digit = int(str(trailing_digit)[-1]))

    # Check if the leading and trailing digits of n are successively removed down to a one- or two-digit prime
    while leading_digit > 0 and trailing_digit > 0:

        if leading_digit == trailing_digit:

            break


        if not is_prime(leading_digit):

            return False


        if not is_prime(trailing_digit):

            return False


        leading_digit = int(str(leading_digit)[0]))

        trailing_digit = int(str(trailing_digit)[-1]))

    # Check if the leading digit of n has been exhausted and the trailing digit of n still remains unexhausted
    if leading_digit == 0:

        return False


    # Check if the trailing digit of n has been exhausted and the leading digit of n still remains unexhausted
    if trailing_digit == 0:

        return False


    # Return True if the leading digit of n is a prime number and the trailing digit of n is a prime number and the leading and trailing digits of n are successively removed down to a one- or two-digit prime
    return True
