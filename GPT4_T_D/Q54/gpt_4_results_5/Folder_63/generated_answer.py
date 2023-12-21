
def all_right_truncatable_prime(number_tuple):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n)):
                return False
            n = n[:-1]
        return True

    n = number_tuple[88]
    result = []
    for i in range(n):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)
