
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        while len(str(n)) > 2:
            n = int(str(n)[1:-1])
            if not is_prime(n):
                return False
        return True

    x = numbers[10]
    truncatable_primes = []
    for num in range(x, 1, -1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes
