
def all_left_truncatable_prime(x):
    # Initialize an empty list to store the results
    prime_numbers = []

    # Loop through all numbers less than x
    for i in range(2, x):
        # Check if the number is a prime number
        if is_prime(i):
            # Check if the number is left-truncatable prime
            if is_left_truncatable_prime(i):
                # Add the number to the list of prime numbers
                prime_numbers.append(i)

    # Return the sorted list of all left-truncatable prime numbers less than x
    return sorted(prime_numbers)

def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop through all numbers less than or equal to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if i divides n
            if n % i == 0:
                # Return False if i divides n
                return False

    # Return True if n is greater than 1 and does not have any factors other than 1 and itself
    return True

def is_left_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        # Return False if n is not a prime number
        return False

    # Initialize an empty string to store the representation of n in base 10
    num_str = ''

    # Loop through all digits of n in base 10
    for digit in str(n):
        # Append each digit of n in base 10 to the string representation of n
        num_str += digit

    # Initialize an empty list to store the resulting numbers if the leading leftmost digit is successively removed
    results = []

    # Loop through all digits of n in base 10
    for i in range(len(num_str)):
        # Append each resulting number to the list of resulting numbers if the leading leftmost digit is successively removed
        results.append(int(num_str[:i] + num_str[i+1:])))

    # Check if all resulting numbers are prime numbers
    for result in results:
        # Return False if any resulting number is not a prime number
        if not is_prime(result):
            return False

    # Return True if all resulting numbers are prime numbers and does not have any factors other than 1 and itself
    return True
