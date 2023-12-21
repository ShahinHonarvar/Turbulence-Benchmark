
def all_left_right_truncatable_prime(x):
    # Create a list of all prime numbers less than or equal to x
    prime_numbers = [p for p in range(2, x + 1) if all(p % i != 0 for i in range(2, int(p ** 0.5) + 1))]
    # Initialize an empty list to store the left-and-right-truncatable prime numbers
    left_right_prime_numbers = []
    # Iterate over the prime numbers and check if they are left-and-right-truncatable prime numbers
    for prime in prime_numbers:
        # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime number
        if all(prime % 10 ** i == 1 for i in range(2)) and all(prime % 10 ** (len(str(prime)) - 1) == 1 for i in range(2)))):
            # If the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime number, add it to the list of left-and-right-truncatable prime numbers
            left_right_prime_numbers.append(prime)
    # Sort the list of left-and-right-truncatable prime numbers in descending order and return it
    return sorted(left_right_prime_numbers, reverse=True)
