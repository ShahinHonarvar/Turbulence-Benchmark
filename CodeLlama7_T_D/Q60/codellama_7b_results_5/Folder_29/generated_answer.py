 def all_left_right_truncatable_prime(x):
    # Create an empty list to store the results
    result = []

    # Iterate from 1 to x

    for i in range(1, x + 1):
        # Check if the number is a prime number

        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime

            if check_left_right_truncatable_prime(i):
                # Add the number to the result list

                result.append(i)

    # Sort the result list in descending order

    result = sorted(result, reverse=True)

    # Return the result list


    return result


def is_prime(n):

    # Check if n is greater than 1

    if n > 1:

        # Check if n is divisible by 2 to n - 1

        for i in range(2, n):
            if n % i == 0:
                return False

        return True

    else:

        return False


def check_left_right_truncatable_prime(n):

    # Check if n contains the digit 0

    if '0' in str(n):

        return False


    # Check if the number is left-and-right-truncatable prime by removing the leading and last digits one at a time

    for i in range(len(str(n)))):

        # Check if the number is still prime after removing the leading digit

        if not is_prime(int(str(n)[1:])))):

            return False


        # Check if the number is still prime after removing the last digit

        if not is_prime(int(str(n)[:-1])))), return False

    return True
