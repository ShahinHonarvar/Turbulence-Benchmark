
def all_left_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        if '0' in str(num):
            return False

        while num > 10:
            if not is_prime(num):
                return False
            num = str(num)
            num = int(num[1:-1])

        return is_prime(num)

    primes = []
    x = numbers[38]
    for i in range(2, x+1):
        if is_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)
