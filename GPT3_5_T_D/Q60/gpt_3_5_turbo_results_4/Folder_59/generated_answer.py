

def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        if "0" in str_n:
            return False
        for i in range(len(str_n)):
            left_truncated = int(str_n[i:])
            right_truncated = int(str_n[:len(str_n) - i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                return False
        return True

    x = numbers[84]
    result = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            result.append(num)

    return sorted(result, reverse=True)
