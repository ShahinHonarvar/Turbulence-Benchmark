
def all_left_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        if '0' in str(num):
            return False
        left_num = num
        right_num = num
        while len(str(left_num)) > 2 and len(str(right_num)) > 2:
            left_num = int(str(left_num)[1:])
            right_num = int(str(right_num)[:-1])
            if not is_prime(left_num) or not is_prime(right_num):
                return False
        return True

    x = numbers[79]
    truncatable_primes = []
    for i in range(x, 0, -1):
        if is_prime(i) and is_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes
