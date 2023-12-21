
def all_left_truncatable_prime(x):
    def is_prime(n):
        if n == 2 or n == 3:
            return True

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False

        return True


    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False

        while len(str(n)) > 1:
            n = int(str(n)[:-1])

            if not is_prime(n):
                return False

        return True


    return [n for n in range(2, x) if is_left_truncatable_prime(n)]
