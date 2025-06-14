
def all_right_truncatable_prime(tuple_of_int):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = n // 10
        return True

    x = tuple_of_int[803]
    res = [i for i in range(2, x) if is_right_truncatable(i)]
    return sorted(res)
