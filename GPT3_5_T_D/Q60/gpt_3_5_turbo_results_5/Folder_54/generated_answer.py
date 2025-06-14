
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        num_digits = len(str(n))
        for i in range(num_digits-1):
            if not is_prime(int(str(n)[i:])):
                return False
            if not is_prime(int(str(n)[:num_digits-i])):
                return False
        return True

    x = numbers[88]
    result = []
    for i in range(x, 0, -1):
        if is_left_right_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result
