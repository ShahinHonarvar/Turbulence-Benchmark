
def all_left_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        str_num = str(num)
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
        return True

    x = numbers[61]
    primes = []
    i = 2
    while len(primes) < x:
        if is_prime(i) and is_left_truncatable_prime(i):
            primes.append(i)
        i += 1

    return primes
