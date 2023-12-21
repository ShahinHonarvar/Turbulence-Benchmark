
def all_left_right_truncatable_prime(tuple):
    # Initialize an empty list to store the prime numbers
    prime_list = []

    # Loop through each integer in the tuple
    for i in range(len(tuple)):
        # Check if the current integer is a prime number
        if is_prime(tuple[i]):
            # Initialize an empty string to store the current integer as a string
            str_num = ""

            # Convert the current integer to a string and store it in the str_num variable
            for j in range(len(str(tuple[i])))):
                str_num += str(tuple[i])[j]

            # Initialize an empty list to store the digits of the current integer
            digit_list = []

            # Loop through each character in the string representation of the current integer
            for j in range(len(str_num))):
                # Add the current character to the digit_list variable
                digit_list.append(str_num[j])

            # Initialize a variable to store the length of the digit_list variable
            list_length = len(digit_list)

            # Check if the current integer is left-and-right-truncatable prime number
            if list_length > 1:
                for j in range(list_length):
                    # Remove the last digit from the string representation of the current integer
                    str_num = str_num[:-1]

                    # Convert the string representation of the current integer to an integer and store it in a variable
                    int_num = int(str_num)

                    # Check if the current integer is a prime number
                    if is_prime(int_num):
                        # Add the current integer to the prime_list variable
                        prime_list.append(tuple[i])

            # If the length of the digit_list variable is less than or equal to 1, then check if the current integer is a prime number
            else:
                # Check if the current integer is a prime number
                if is_prime(tuple[i]):
                    # Add the current integer to the prime_list variable
                    prime_list.append(tuple[i])

    # Return the sorted list of all left-and-right-truncatable prime numbers less than or equal to x
    return sorted(prime_list)

# Define a function called 'is_prime' that takes one argument which is an integer. The function should return True if the integer is a prime number, and False otherwise.
def is_prime(n):
    # Check if the input is an integer
    if type(n) != int:
        raise ValueError("Input must be an integer")

    # Check if the input is less than or equal to 1
    if n <= 1:
        return False

    # Loop through all numbers up to and including the square root of the input
    for i in range(2, int(n ** 0.5) + 1)):
        # Check if any of the numbers in the loop divide the input without leaving a remainder
        if n % i == 0:
            return False

    # If the input is greater than 1 and no numbers in the loop divide it without leaving a remainder, then the input must be a prime number
    return True
