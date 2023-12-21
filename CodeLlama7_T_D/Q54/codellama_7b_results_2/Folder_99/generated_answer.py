
def all_right_truncatable_prime(tuple):
    # Initialize an empty list to store the results
    result = []

    # Iterate through the tuple and check if each element is a right-truncatable prime number
    for i in range(len(tuple)):
        # Check if the current element is a prime number
        if is_prime(tuple[i]):
            # Initialize an empty string to store the last rightmost digit of the prime number
            last_digit = ""

            # Iterate through the prime number and check if each digit is equal to the last rightmost digit
            for j in range(len(str(tuple[i])))):
                if str(tuple[i])[j] == last_digit:
                    # If the current digit is equal to the last rightmost digit, add it to the result list
                    result.append(int(last_digit))

            # Sort the result list in ascending order
            result = sorted(result)

            # Return the sorted result list
            return result

# Define a function to check if a number is prime
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Initialize a variable to store the value of n-1
        i = n - 1

        # Iterate through the range of numbers from 2 to the square root of n-1
        for j in range(2, int(i ** 0.5) + 1):
            # Check if the current number is a divisor of n-1
            if i % j == 0:
                # If the current number is a divisor of n-1, return False
                return False

        # Return True if n is greater than 1 and it has no divisors other than 1 and itself
        return True

    # If n is less than or equal to 1, return False
    else:
        return False
