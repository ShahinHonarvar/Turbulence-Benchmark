
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[29]

    def is_left_truncatable(n):
        while n > 9:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        return True

    def is_right_truncatable(n):
        while n > 9:
            n = int(str(n)[:-1])
            if not is_prime(n):
                return False
        return True

    truncatable_primes = []
    for num in range(x, 0, -1):
        if num % 10 != 0 and is_prime(num) and is_left_truncatable(num) and is_right_truncatable(num):
            truncatable_primes.append(num)

    return truncatable_primes
