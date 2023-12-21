
def all_left_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Check if x is a prime number and add it to the list if it is
    if is_prime(x):
        prime_numbers.append(x)

    # Remove the leading leftmost digit of x and check if the resulting number is a prime number
    for i in range(1, len(str(x)))):
        y = int(str(x)[i:])
        if is_prime(y):
            prime_numbers.append(y)

    # Remove the leading leftmost digit of each prime number and check if the resulting number is a prime number
    for i in range(len(prime_numbers)):
        y = int(str(prime_numbers[i])[1:]))
        if is_prime(y):
            prime_numbers.append(y)

    # Return the sorted list of all left-truncatable prime numbers less than x
    return sorted(prime_numbers)
