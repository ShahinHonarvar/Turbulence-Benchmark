
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for num in numbers:
        if num < 10 or '0' in str(num):
            continue
        is_left_truncatable = True
        str_num = str(num)
        while str_num:
            if not is_prime(int(str_num)):
                is_left_truncatable = False
                break
            str_num = str_num[1:]
        if is_left_truncatable:
            primes.append(num)
    primes.sort()
    return primes
