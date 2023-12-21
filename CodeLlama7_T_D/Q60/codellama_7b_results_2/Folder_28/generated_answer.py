
def all_left_right_truncatable_prime(x):
    # Create a list of all prime numbers less than or equal to x
    prime_numbers = [p for p in range(2, x + 1) if all(p % i != 0 for i in range(2, int(p ** 0.5) + 1))]
    # Filter the list to include only left-and-right-truncatable prime numbers
    return [p for p in prime_numbers if len(str(p)) > 1 and str(p).startswith('1') and str(p).endswith('1')]
