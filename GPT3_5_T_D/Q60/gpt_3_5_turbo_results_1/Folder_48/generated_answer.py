
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[835]
    primes = []
    
    def is_left_truncatable(n):
        while n > 9:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return is_prime(n)
    
    def is_right_truncatable(n):
        while n > 9:
            if not is_prime(n):
                return False
            n = int(str(n)[:-1])
        return is_prime(n)
    
    for num in range(2, x+1):
        if '0' in str(num):
            continue
        if is_left_truncatable(num) and is_right_truncatable(num):
            primes.append(num)
    
    primes.sort()
    return primes
