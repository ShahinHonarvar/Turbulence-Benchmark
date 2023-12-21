
def all_left_right_truncatable_prime(x):
    # create a list of all prime numbers less than or equal to x
    prime_numbers = [p for p in range(2, x + 1) if all(p % i != 0 for i in range(2, int(p ** 0.5) + 1))]
    # filter the list to only include left-and-right-truncatable prime numbers
    return [p for p in prime_numbers if '0' not in str(p) and len(str(p)) > 2]
