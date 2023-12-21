
def all_left_truncatable_prime(tup):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n**0.5)
        for d in range(3, max_divisor + 1, 2):
            if n % d == 0:
                return False
        return True

    def left_truncatable(n):
        if '0' in str(n):
            return False

        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True

    x = tup[86]
    return sorted([i for i in range(2, x) if left_truncatable(i)])
