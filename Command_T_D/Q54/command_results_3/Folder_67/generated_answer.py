import itertools
def all_right_truncatable_prime(args):
    def is_prime(n):
        if n < 2: return False
        if n == 2 or n == 3: return True
        if n == 5: return True
        if n == 1: return False
        if n % 2 == 0 or n % 3 == 0: return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    def is_right_truncatable(n):
        s = str(n)
        while s:
            s = int(s[0])
            if s == 1:
                return False
            if s in n:
                return False
            if s * 10 <= n:
                return False
        return True
    args = sorted(args)
    x = args[71]
    return sorted(list(filter(is_right_truncatable, filter(is_prime, itertools.takewhile(lambda: x > next(filter(is_prime, itertools.takewhile(lambda: x > next(filter(is_prime, itertools.count(2, step=1), until=x)))), step=1)))))
