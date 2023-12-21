
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the results
    result = []

    # Iterate over each number in the range from 2 to x (inclusive)
    for i in range(2, x + 1):
        # Check if the current number is a left-and-right-truncatable prime
        if is_left_right_truncatable_prime(i):
            # If it is, add it to the result list
            result.append(i)

    # Return the sorted result list (in descending order)
    return sorted(result, reverse=True)

def is_left_right_truncatable_prime(n):
    # Check if the number contains a 0 digit
    if '0' in str(n):
        return False

    # Iterate over each digit in the number (from left to right and from right to left)
    for i in range(len(str(n))):
        # Check if the current digit is not a 0 digit
        if str(n)[i] != '0':
            # If it is, check if the resulting number is prime
            if not is_prime(int(str(n)[:i] + str(n)[i+1:])):
                return False

    # If all digits are 0 digits or the number is a one-digit prime, return True
    return True

def is_prime(n):
    # Check if the number is divisible by any number between 2 and its square root (inclusive)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # If the number is not divisible by any other number, return True
    return True
