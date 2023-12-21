
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
        if '0' in s:
            return False
        while s:
            if not is_prime(int(s)):
                return False
            s = s[1:]
        s = str(n)
        while s:
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        return True

    x = numbers[31]
    result = []
    for i in range(x, 0, -1):
        if is_truncatable_prime(i):
            result.append(i)

    result.sort(reverse=True)
    return result
