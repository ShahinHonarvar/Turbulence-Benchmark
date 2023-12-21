
def all_left_right_truncatable_prime(x):
    # Find all prime numbers less than or equal to x
    prime_numbers = [p for p in range(2, x + 1) if all(p % i != 0 for i in range(2, int(p ** 0.5) + 1))]
    # Filter out non-left-and-right-truncatable prime numbers
    left_right_truncatable_prime_numbers = [p for p in prime_numbers if all(str(p)[i] == str(p)[-i - 1] for i in range(len(str(p)))) and len(str(p)) > 1]]
    # Sort the remaining prime numbers in descending order
    sorted_left_right_truncatable_prime_numbers = sorted(left_right_truncatable_prime_numbers, reverse=True)
    return sorted_left_right_truncatable_prime_numbers
