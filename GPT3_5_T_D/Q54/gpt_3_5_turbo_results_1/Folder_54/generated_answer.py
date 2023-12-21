
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[88]
    right_truncatable_primes = []

    for num in range(2, x):
        if is_prime(num):
            is_right_truncatable_prime = True
            temp_num = num

            while temp_num > 0:
                if not is_prime(temp_num):
                    is_right_truncatable_prime = False
                    break
                temp_num //= 10

            if is_right_truncatable_prime:
                right_truncatable_primes.append(num)

    return sorted(right_truncatable_primes, reverse=True)
