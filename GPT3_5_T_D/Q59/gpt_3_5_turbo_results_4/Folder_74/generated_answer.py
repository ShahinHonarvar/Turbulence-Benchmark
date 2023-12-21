
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
        while str_num:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[1:]
        return True

    x = numbers[36]

    left_truncatable_primes = []
    for i in range(2, x):
        if i == 2 or i == 3 or i == 5 or i == 7:
            left_truncatable_primes.append(i)
        elif is_prime(i) and is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)

    return sorted(left_truncatable_primes)
