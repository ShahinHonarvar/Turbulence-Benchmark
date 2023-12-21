
def all_right_truncatable_prime(tuple_input):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True

    def is_right_truncatable(n):
        while n != 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    x = tuple_input[79]
    return sorted([i for i in range(x) if is_right_truncatable(i)], reverse=True)
