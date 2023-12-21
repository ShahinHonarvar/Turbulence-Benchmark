
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if '0' in str_n[i:]:
                return False
            if not is_prime(int(str_n[i:])):
                return False
        return True

    x = numbers[39]
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)

    return sorted(result)
