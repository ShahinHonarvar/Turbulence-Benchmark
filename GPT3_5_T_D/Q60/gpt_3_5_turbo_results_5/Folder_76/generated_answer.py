
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
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:i])):
                return False
        return True

    x = numbers[370]
    truncatable_primes = []
    for num in range(x, 0, -1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes
