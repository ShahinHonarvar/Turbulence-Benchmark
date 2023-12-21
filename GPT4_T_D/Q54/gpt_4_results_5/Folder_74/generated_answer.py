
def all_right_truncatable_prime(numbers):
    x = numbers[36]
    def check_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_truncatable(n):
        for i in range(len(str(n))):
            if not check_prime(int(str(n)[i:])):
                return False
        return True
    
    truncatable_primes = []    
    for n in range(x):
        if check_truncatable(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes)
