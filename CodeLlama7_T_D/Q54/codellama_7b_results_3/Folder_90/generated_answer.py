
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the tuple of positive integers
    for i in range(len(tuple)):
        # Get the current integer from the tuple
        num = tuple[i]

        # Check if the current number is a prime number
        if is_prime(num):
            # Initialize an empty string to store the current number as a string
            str_num = ''

            # Convert the current number to a string and store it in the string variable
            for j in range(len(str(num)))):
                # Get the current character from the string representation of the number
                char = str(num)[j]

                # If the current character is not the last character, append it to the string variable
                if j < len(str(num))) - 1:
                    str_num += char

            # Check if the string representation of the number still satisfies the prime condition after removing the rightmost digit
            if is_prime(int(str_num))):
                result.append(int(str_num)))

    # Sort the results in descending order and return them
    return sorted(result, reverse=True)

# Function to check if a number is prime
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1 without finding any factors
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If n is a prime number, it is greater than 1
    return True
