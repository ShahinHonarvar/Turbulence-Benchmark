 def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the results
    result = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-right truncatable
            if is_left_right_truncatable(i):
                # Add the number to the result list
                result.append(i)

    # Sort the result list in descending order
    result.sort(reverse=True)

    # Return the result list
    return result

def is_prime(n):

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If the loop completes successfully, return True
    return True

def is_left_right_truncatable(n):

    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n contains any zeros
    if '0' in str(n):
        return False

    # Get the length of the number of digits in n
    num_digits = len(str(n))

    # Check if the leading digit is 1 or greater
    if int(str(n)[0]) < 1:
        return False

    # Check if the last rightmost digit is equal to the first leftmost digit
    if int(str(n)[-1]) != int(str(n)[0])):
        return False

    # If all previous conditions are met, return True
    return True
