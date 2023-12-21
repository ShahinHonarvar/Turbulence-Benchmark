
def all_left_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(1, len(str_num)):
            left = int(str_num[i:])
            right = int(str_num[:-i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True

    x = numbers[89]
    truncatable_primes = [num for num in range(2, x + 1) if is_truncatable_prime(num)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
