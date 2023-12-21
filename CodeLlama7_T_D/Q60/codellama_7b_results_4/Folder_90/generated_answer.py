 def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_list = []
    # Loop through all numbers less than or equal to x
    for i in range(1, x + 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_list.append(i)
    # Sort the list in descending order
    prime_list.sort(reverse=True)
    return prime_list

def is_left_right_truncatable_prime(n):
    # Check if the number contains any 0 digits
    if "0" in str(n):
        # If the number contains any 0 digits, it is not a left-and-right-truncatable prime number
        return False

    # Check if the number is a prime number

    if is_prime(n):
        # Check if the number is divisible by 11

        if n % 11 == 0:
            # If the number is divisible by 11, it is not a left-and-right-truncatable prime number
            return False

    # Check if the number is a palindrome

    if str(n) == str(n)[::-1]:
        # Check if the number has at least three digits

        if len(str(n)) >= 3:
            # Check if the number has no leading leftmost or last rightmost digits that are not consecutive

            if (str(n)[:2] != "10" and str(n)[:2] != "11") and (str(n)[-2:] != "10" and str(n)[-2:] != "11"):
                # Check if the number has no leading leftmost or last rightmost digits that are not consecutive

                if not any(str(n)[:i] == str(n)[-(i + 1):] for i in range(3, len(str(n))) if (str(n)[:i] != "0" and str(n)[:i] != "1") and (str(n)[-(i + 1):] != "0" and str(n)[-(i + 1):] != "1")):
                    # If the number is a left-and-right-truncatable prime number, return True

                    return True

    # If the number is not a left-and-right-truncatable prime number, return False

    return False

def is_prime(n):

    # Check if the number is less than 2

    if n < 2:

        # If the number is less than 2, it is not a prime number

        return False

    # Check if the number is divisible by any number between 2 and the square root of the number

    for i in range(2, int(n ** 0.5) + 1):

        # If the number is divisible by any number between 2 and the square root of the number, it is not a prime number

        if n % i == 0:

            return False

    # If the number passes all previous tests, it is a prime number

    return True
