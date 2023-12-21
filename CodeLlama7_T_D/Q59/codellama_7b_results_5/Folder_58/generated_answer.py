
def all_left_truncatable_prime(tuple):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the tuple elements
    for element in tuple:
        # Check if the current element is a prime number
        if is_prime(element):
            # Add the current element to the result list
            result.append(element)

        # While iterating, also check if any of the resulting numbers are left-truncatable prime numbers
        while len(result) > 0:
            # Get the last number in the result list
            last_number = result[-1]

            # Check if the last number is a left-truncatable prime number
            if is_left_truncatable_prime(last_number):
                # Add the last number to the result list
                result.append(last_number)

            # Remove the last number from the result list
            result = result[:-1]

    return sorted(result, reverse=True)

def is_prime(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    # If the number is not a prime number, it cannot be a left-truncatable prime number
    if not is_prime(n):
        return False

    # Check if the number contains any 0 digits
    if "0" in str(n):
        return False

    # Check if the number is a left-truncatable prime number by removing the leading leftmost digit and checking if all resulting numbers are prime
    for i in range(1, len(str(n)))):
        current_number = int(str(n)[:i] + str(n)[i+1:]))
        if not is_prime(current_number):
            return False

    # If all checks pass, the number is a left-truncatable prime number
    return True
