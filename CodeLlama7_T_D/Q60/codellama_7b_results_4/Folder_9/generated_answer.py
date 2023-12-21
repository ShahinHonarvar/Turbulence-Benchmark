
def all_left_right_truncatable_prime(x):
    # Create a list of all prime numbers less than or equal to x
    prime_numbers = [p for p in range(2, x + 1) if all(p % i != 0 for i in range(2, int(p ** 0.5) + 1))]
    # Filter the list to only include left-and-right-truncatable prime numbers
    left_right_truncatable_prime_numbers = [p for p in prime_numbers if all([int(str(p)[i]) == int(str(p)[i + 1]) for i in range(len(str(p)))])]
    # Sort the list in descending order
    left_right_truncatable_prime_numbers.sort(reverse=True)
    return left_right_truncatable_prime_numbers
