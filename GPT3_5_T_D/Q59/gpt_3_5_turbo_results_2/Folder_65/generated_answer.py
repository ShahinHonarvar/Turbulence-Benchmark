
def all_left_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    x = numbers[32]
    primes = []
    for num in range(2, x):
        if '0' not in str(num):
            left_truncatable = True
            for i in range(len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    left_truncatable = False
                    break
            if left_truncatable:
                primes.append(num)
    return sorted(primes)
