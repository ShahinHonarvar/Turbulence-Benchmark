
def all_left_right_truncatable_prime(x):
    def is_left_right_truncatable_prime(n):
        if n < 2:
            return False

        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        digits = [int(d) for d in str(n)]
        for i in range(len(digits)):
            if digits[i] == 0:
                return False

            if digits[-1 - i] != digits[i]:
                return False

        return True

    return [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
