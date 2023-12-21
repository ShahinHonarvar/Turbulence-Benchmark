
def all_left_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            left_truncated = int(str_num[i:])
            right_truncated = int(str_num[:len(str_num) - i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                return False
        return True

    x = numbers[10] if len(numbers) > 10 else 0
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)
