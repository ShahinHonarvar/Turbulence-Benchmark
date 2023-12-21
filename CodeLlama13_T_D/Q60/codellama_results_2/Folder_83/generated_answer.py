
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncatable_prime(n):
        if len(str(n)) <= 3 or not is_prime(n):
            return False
        for i in range(len(str(n)) - 1, 0, -1):
            if not is_prime(int(str(n)[:i])):
                return False
        for j in range(2, len(str(n))):
            if not is_prime(int(str(n)[j:])):
                return False
        return True

    result = []
    for n in numbers:
        if truncatable_prime(n):
            result.append(n)
    return sorted(result)
