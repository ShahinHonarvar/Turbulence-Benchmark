
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[25]
    right_truncatable_primes = []
    
    def check_right_truncatable_prime(num):
        if not is_prime(num):
            return False
        while num > 9:
            num = num // 10
            if not is_prime(num):
                return False
        return True
    
    for i in range(x-1, 9, -1):
        if check_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    
    return sorted(right_truncatable_primes, reverse=True)
