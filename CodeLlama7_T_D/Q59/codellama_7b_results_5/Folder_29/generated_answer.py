 def all_left_truncatable_prime(tuple):
    # Initialize variables
    x = tuple[55]
    prime_numbers = []

    # Loop through numbers from 1 to x - 1
    for i in range(1, x - 1):
        # Check if the number is a prime number
        if is_prime(i):
            # Add the prime number to the list
            prime_numbers.append(i)

    # Loop through each number in the list of prime numbers
    for i in range(len(prime_numbers)):
        # Check if the number is left-truncatable prime
        if is_left_truncatable_prime(prime_numbers[i]):
            # Add the number to the final list of left-truncatable prime numbers
            final_list.append(prime_numbers[i])

    # Sort the final list in descending order
    final_list.sort(reverse=True)

    # Return the final list of left-truncatable prime numbers
    return final_list

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_truncatable_prime(n):
    # Initialize variables
    num = n
    leading_digit = int(str(num)[0])

    # Check if the number contains no 0
    if '0' in str(num):
        return False

    # Remove the leading leftmost digit from the number until all digits are removed
    while len(str(num)) > 1:
        num = int(str(num)[1:])

    # Check if the resulting number is a prime number
    if is_prime(num):
        return True

    else:
        return False
