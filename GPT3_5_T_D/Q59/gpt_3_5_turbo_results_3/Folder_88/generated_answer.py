
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_truncatable_prime(number):
        for i in range(len(number)):
            if not is_prime(int(number[i:])):
                return False
        return True
    
    x = numbers[93]
    primes = []
    
    for num in range(2, x):
        if '0' not in str(num) and is_truncatable_prime(str(num)):
            primes.append(num)
    
    return sorted(primes)
