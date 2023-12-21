
def all_right_truncatable_prime(tuples):
    def is_prime(n):
        if n == 1:
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

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n != 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    x = tuples[20]
    result = []
    for i in range(x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
