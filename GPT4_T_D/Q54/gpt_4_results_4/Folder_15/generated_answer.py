
def all_right_truncatable_prime(tup):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str)):
            if not is_prime(int(n_str[:len(n_str)-i])):
                return False
        return True

    x = tup[6]
    result = []
    for i in range(2, x):
        if is_right_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)
