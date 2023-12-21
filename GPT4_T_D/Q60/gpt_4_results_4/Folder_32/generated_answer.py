
def all_left_right_truncatable_prime(numbers):
    from sympy import isprime

    x = numbers[42]

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False

        for i in range(len(s)):
            if not isprime(int(s[i:])) or not isprime(int(s[:i+1])):
                return False
        return True

    return sorted(n for n in range(10, x + 1) if is_truncatable_prime(n))
