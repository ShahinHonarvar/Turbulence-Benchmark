
def all_left_right_truncatable_prime(numbers):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def is_truncatable_prime(number):
        str_number = str(number)
        if '0' in str_number:
            return False
        for i in range(1, len(str_number)):
            left_trunc = int(str_number[i:])
            right_trunc = int(str_number[:-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True

    x = numbers[54]
    truncatable_primes = []
    for i in range(x, 1, -1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return truncatable_primes
