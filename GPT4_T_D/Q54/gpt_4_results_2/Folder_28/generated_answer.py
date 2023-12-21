
def all_right_truncatable_prime(tup):

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

    def is_r_truncatable(n):
        if not is_prime(n):
            return False
        while n != 0:
            n = n // 10
            if not is_prime(n) and n != 0:
                return False
        return True

    x = tup[19]
    result = [i for i in range(x) if is_r_truncatable(i)]

    return sorted(result)
