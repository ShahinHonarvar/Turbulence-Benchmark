
def all_right_truncatable_prime(t):
    x = t[98]
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    def right_truncatable(n):
        while n > 0:
            if is_prime(n):
                n //= 10
            else:
                return False
        return True
    truncatables = []
    for i in range(x):
        if right_truncatable(i):
            truncatables.append(i)
    return sorted(truncatables)
