
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[97]
    right_truncatable_primes = []

    for num in range(x-1, 10, -1):
        if is_prime(num):
            num_str = str(num)
            n = len(num_str)

            while n > 0:
                if not is_prime(int(num_str[:n])):
                    break
                n -= 1
            else:
                right_truncatable_primes.append(num)

    return sorted(right_truncatable_primes, reverse=True)
