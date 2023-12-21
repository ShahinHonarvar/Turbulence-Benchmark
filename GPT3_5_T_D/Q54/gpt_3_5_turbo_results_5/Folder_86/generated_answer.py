
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[126]
    right_truncatable_primes = []

    def check_right_truncatable_prime(num):
        if is_prime(num):
            right_truncatable_primes.append(num)
            for digit in range(10):
                new_num = num * 10 + digit
                if is_prime(new_num):
                    check_right_truncatable_prime(new_num)

    check_right_truncatable_prime(2)

    return sorted(right_truncatable_primes, reverse=True)
