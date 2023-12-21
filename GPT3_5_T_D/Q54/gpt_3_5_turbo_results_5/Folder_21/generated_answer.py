
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[175]

    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            while len(num_str) > 1:
                num_str = num_str[:-1]
                if not is_prime(int(num_str)):
                    break
            else:
                right_truncatable_primes.append(num)

    return right_truncatable_primes
