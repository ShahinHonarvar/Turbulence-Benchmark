
def all_right_truncatable_prime(tup):
    x = tup[81]

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for current in range(3, int(n ** 0.5) + 1, 2):
            if n % current == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n[i:])):
                return False
        return True

    res = []
    for n in range(x):
        if is_truncatable_prime(n):
            res.append(n)

    return sorted(res, reverse=True)
