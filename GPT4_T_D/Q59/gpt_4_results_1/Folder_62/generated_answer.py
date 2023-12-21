
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True

    x = numbers[70]
    return sorted([n for n in range(1, x) if is_left_truncatable(n)])
