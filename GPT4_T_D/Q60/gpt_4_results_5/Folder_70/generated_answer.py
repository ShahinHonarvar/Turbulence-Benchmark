
def all_left_right_truncatable_prime(t):
    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s)-i])):
                return False
        return True

    x = t[433]
    result = [i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)]
    result.sort(reverse = True)
    return result
