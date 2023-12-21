
def all_left_right_truncatable_prime(tup):
    x = tup[85]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:i])):
                return False
        return True

    truncatables = []
    for i in range(11, x + 1, 2):
        if is_prime(i) and is_left_right_truncatable(i):
            truncatables.append(i)
    return truncatables
