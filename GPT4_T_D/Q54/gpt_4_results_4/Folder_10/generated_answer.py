
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**(0.5)) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        str_num = str(n)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[:i])):
                return False
        return True

    x = numbers[38]
    result = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
