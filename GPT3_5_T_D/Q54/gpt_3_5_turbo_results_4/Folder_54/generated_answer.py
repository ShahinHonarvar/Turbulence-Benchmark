
def all_right_truncatable_prime(numbers):
    def is_prime(num):
        if num == 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    x = numbers[88]
    right_truncatable_primes = []
    for num in range(x - 1, 10, -1):
        if is_prime(num):
            right_truncatable = True
            str_num = str(num)
            while str_num:
                if not is_prime(int(str_num)):
                    right_truncatable = False
                    break
                str_num = str_num[:-1]
            if right_truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)
