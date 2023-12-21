
def all_left_truncatable_prime(tuple):
    # Initialize variables
    x = tuple[65]
    list = []
    # Iterate through numbers less than x
    for i in range(2, x):
        # Check if number is prime
        if is_prime(i):
            # Check if number is left-truncatable prime
            if is_left_truncatable_prime(i):
                # Add number to list
                list.append(i)
    # Sort list in descending order
    list.sort(reverse=True)
    return list

# Check if number is prime
def is_prime(n):
    # Check if number is less than 2
    if n < 2:
        return False

    # Check if number is divisible by 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    # If number is greater than 1 and it is not divisible by any prime number less than or equal to its square root, it is prime
    return True

# Check if number is left-truncatable prime
def is_left_truncatable_prime(n):
    # Convert number to string
    s = str(n)

    # Iterate through characters in string
    for i in range(len(s)):
        # Check if character is 0
        if s[i] == '0':
            return False

        # Check if character is last character in string
        if i == len(s) - 1:
            continue

        # Check if next character in string is not a prime number
        if not is_prime(int(s[i + 1]))):
            return False

    # If number is left-truncatable prime, it passes all checks
    return True
