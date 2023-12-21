
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[24]
    truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            temp = str(i)
            while temp:
                if not is_prime(int(temp)):
                    break
                temp = temp[:-1]
            else:
                truncatable_primes.append(i)
    return sorted(truncatable_primes)
