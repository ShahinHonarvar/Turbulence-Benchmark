
def all_right_truncatable_prime(t):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if not is_prime(n):
            return False
        for i in range(1, len(str(n))):
            if not is_prime(int(str(n)[:-i])):
                return False
        return True

    x = t[92]
    result = []
    for num in range(2, x):
        if is_truncatable(num):
            result.append(num)
    return sorted(result)
