
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 1 to x
    for i in range(1, x + 1):
        # Check if i is a prime number
        if is_prime(i):
            # Check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # Add i to the list of prime numbers
                prime_numbers.append(i)

    # Sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # Return the list of prime numbers
    return prime_numbers

# Check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # If i divides n, return False
                return False

    # If n is greater than 1 and has no factors other than 1 and itself, return True
    return True

# Check if a number is left-and-right-truncatable prime number
def is_left_right_truncatable_prime(n):
    # Check if n is greater than 2
    if n > 2:
        # Initialize an empty string to store the digits of n in reverse order
        digits = ""

        # Iterate from the last digit of n to the first digit
        for i in range(len(str(n))), -1, -1):
            # Add the current digit to the end of the string
            digits += str(n)[i]

        # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
        if len(str(n)) == 1:
            # If n has only one digit, return True
            return True

        elif len(str(n)) == 2:
            # If n has two digits, check if the leading leftmost and last rightmost digits are both equal to 0 or 1
            if str(n)[0] == "0" or str(n)[0] == "1":
                # If the leading leftmost digit is equal to 0 or 1, return True
                return True

            else:
                # If the leading leftmost digit is not equal to 0 or 1, return False
                return False

        elif len(str(n)) > 2:
            # If n has more than two digits, check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one-digit prime
            for i in range(len(str(n)))):
                # Remove the current digit from the end of the string
                digits = str(n)[0:i] + str(n)[i + 1:]

                # Check if the remaining digits form a valid one-digit prime number
                if len(digits) == 1 and is_prime(int(digits))):
                    # If the remaining digits form a valid one-digit prime number, return True
                    return True

            # If the leading leftmost and last rightmost digits are not simultaneously successively removed down to a one-digit prime number, return False
            return False
