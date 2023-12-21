
def all_left_right_truncatable_prime(t):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
            if not is_prime(int(s[:i+1])):
                return False
        return True

    x = t[70]
    result = []
    for num in range(2, x+1):
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result)
