
def all_left_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        string_num = str(num)
        if '0' in string_num:
            return False
        for i in range(1, len(string_num)):
            if not is_prime(int(string_num[i:])) or not is_prime(int(string_num[:i])):
                return False
        return True

    x = numbers[32]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)
