
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[3]
    right_truncatable_primes = []

    for num in range(2, x):
        if is_prime(num):
            truncatable_prime = True
            str_num = str(num)
            while len(str_num) > 1:
                str_num = str_num[:-1]
                if not is_prime(int(str_num)):
                    truncatable_prime = False
                    break
            if truncatable_prime:
                right_truncatable_primes.append(num)

    return sorted(right_truncatable_primes, reverse=True)
