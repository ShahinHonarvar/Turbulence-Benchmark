
def all_right_truncatable_prime(t):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    def is_right_truncatable(x):
        for i in range(len(str(x))):
            if not is_prime(int(str(x)[:len(str(x)) - i])):
                return False
        return True

    x = t[645]

    return sorted([i for i in range(x) if is_right_truncatable(i)])
