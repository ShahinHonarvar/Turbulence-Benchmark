
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    truncatable_primes = []
    
    def is_left_right_truncatable_prime(num):
        if '0' in str(num):
            return False
        while len(str(num)) > 2:
            if not is_prime(num):
                return False
            num = int(str(num)[1:-1])
        return True
    
    for num in range(x, 0, -1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    
    return truncatable_primes
