
def all_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    x = numbers[11]
    right_truncatable_primes = []

    def check_right_truncatable(num):
        if not is_prime(num):
            return
        right_truncatable_primes.append(num)
        for i in range(10):
            new_num = num * 10 + i
            check_right_truncatable(new_num)

    for i in range(2, 10):
        check_right_truncatable(i)

    return sorted([p for p in right_truncatable_primes if p < x])
