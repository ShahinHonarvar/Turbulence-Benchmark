
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        if not is_prime(n):
            return False
        n = str(n)
        while len(n) > 1:
            n = n[1:-1]
            if not is_prime(int(n)):
                return False
        return True

    x = numbers[94]
    result = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result)
