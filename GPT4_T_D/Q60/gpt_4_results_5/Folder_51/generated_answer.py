
def all_left_right_truncatable_prime(t):
    x = t[54]

    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            left = int(str(n)[i:])
            right = int(str(n)[: len(str(n)) - i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True

    truncated = [i for i in range(x+1) if is_prime(i) and is_truncatable(i)]
    truncated.sort()
    return truncated
