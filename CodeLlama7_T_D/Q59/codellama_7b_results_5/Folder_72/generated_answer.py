
def all_left_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from x-1 to 1
    for i in range(x-1, 1, -1):
        # Check if the number is a prime number
        if is_prime(i):
            # Add the prime number to the list
            prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers, reverse=True)

# Function to check if a number is a prime number
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Check if n is divisible by 2 to n-1
        for i in range(2, n):
            if n % i == 0:
                return False

    # If the number is greater than 1 and it is not divisible by any prime number in the range, then it is a prime number
    return True
