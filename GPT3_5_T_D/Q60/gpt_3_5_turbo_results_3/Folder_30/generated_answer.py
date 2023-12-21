
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
            if not is_prime(int(str(n)[:i+1])):
                return False
        return True

    x = numbers[37]
    result = []
    for i in range(x, 0, -1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
