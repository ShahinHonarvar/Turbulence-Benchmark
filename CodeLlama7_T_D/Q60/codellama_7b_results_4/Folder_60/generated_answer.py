
def all_left_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Loop through each integer in the tuple
    for i in range(len(tuple)):

        # Get the current integer
        integer = tuple[i]

        # Check if the integer is a prime number
        if is_prime(integer):

            # Initialize an empty string to store the left-and-right-truncatable prime numbers
            left_right_truncatable_prime_numbers = ""

            # Loop through each digit in the integer
            for j in range(len(str(integer)))):

                # Get the current digit
                digit = str(integer)[j]

                # Check if the digit is not 0
                if digit != "0":

                    # Append the left-and-right-truncatable prime numbers to the empty string
                    left_right_truncatable_prime_numbers += str(digit)

            # Check if the length of the left-and-right-truncatable prime numbers is greater than or equal to 2
            if len(left_right_truncatable_prime_numbers) >= 2:

                # Initialize a variable to store the integer with the leading leftmost and last rightmost digits removed
                integer_with_leading_and_last_digits_removed = int(left_right_truncatable_prime_numbers)

                # Check if the integer with the leading leftmost and last rightmost digits removed is a prime number
                if is_prime(integer_with_leading_and_last_digits_removed):

                    # Add the current integer to the list of prime numbers
                    prime_numbers.append(integer)

            # Check if the length of the left-and-right-truncatable prime numbers is greater than or equal to 3
            elif len(left_right_truncatable_prime_numbers) >= 3:

                # Initialize a variable to store the integer with the leading leftmost and last rightmost digits removed
                integer_with_leading_and_last_digits_removed = int(left_right_truncatable_prime_numbers[1:-1])

                # Check if the integer with the leading leftmost and last rightmost digits removed is a prime number
                if is_prime(integer_with_leading_and_last_digits_removed):

                    # Add the current integer to the list of prime numbers
                    prime_numbers.append(integer)

    # Sort the list of prime numbers in ascending order
    sorted_prime_numbers = sorted(prime_numbers)

    # Return the sorted list of prime numbers
    return sorted_prime_numbers

# Test the function with a tuple containing integers from 1 to 100
#print(all_left_right_truncatable_prime((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100))

# Find all left-and-right-truncatable prime numbers less than or equal to the specified integer
def left_right_truncatable_prime(integer):

    # Initialize a list to store the prime numbers
    prime_numbers = []

    # Check if the specified integer is a prime number
    if is_prime(integer):

        # Add the specified integer to the list of prime numbers
        prime_numbers.append(integer)

    # Loop over all possible ways of removing leading and last digits from the specified integer
    for i in range(1, integer + 1):

        # Initialize a variable to store the integer with the leading leftmost and last rightmost digits removed
        integer_with_leading_and_last_digits_removed = int(str(integer)[i:] + str(integer)[:i])

        # Check if the integer with the leading leftmost and last rightmost digits removed is a prime number
        if is_prime(integer_with_leading_and_last_digits_removed):

            # Add the current integer to the list of prime numbers
            prime_numbers.append(integer)

    # Sort the list of prime numbers in ascending order
    sorted_prime_numbers = sorted(prime_numbers)

    # Return the sorted list of prime numbers
    return sorted_prime_numbers
