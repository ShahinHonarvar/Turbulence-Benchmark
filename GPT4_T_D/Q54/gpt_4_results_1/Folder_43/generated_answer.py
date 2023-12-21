
def all_right_truncatable_prime(t):
    def is_prime(n):
        if n == 1 or (n != 2 and n % 2 == 0):
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    x = t[89]
    result = [i for i in range(2, x) if is_right_truncatable_prime(i)]
    result.sort(reverse=True)
    return result
