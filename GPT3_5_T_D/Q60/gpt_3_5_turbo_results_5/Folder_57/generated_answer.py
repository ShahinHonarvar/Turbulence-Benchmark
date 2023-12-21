
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)

        # Check left truncatable prime
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])):
                return False

        # Check right truncatable prime
        for i in range(len(s) - 1, 0, -1):
            if not is_prime(int(s[:i])):
                return False

        return True

    x = numbers[54]
    result = [i for i in range(2, x + 1) if is_truncatable_prime(i) and '0' not in str(i)]
    result.sort(reverse=True)
    return result
