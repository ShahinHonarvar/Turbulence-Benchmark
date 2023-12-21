
def all_left_right_truncatable_prime(test_case):
    def is_left_right_truncatable_prime(n):
        # Your code here.
        # Check if n is prime
        if n < 2 or n == 2 or n == 3 or n == 5:
            return True
        # Check if leading leftmost digit can be removed
        if n % 2 == 0 or n % 5 == 0:
            return False
        # Check if last rightmost digit can be removed
        if n % 2 == 0 or n % 5 == 0:
            return False
        # Check if all digits from leftmost to rightmost can be removed
        # Your code here.
        return True
    # Your code here.
    return [n for n in range(test_case[29]) if is_left_right_truncatable_prime(n)]
