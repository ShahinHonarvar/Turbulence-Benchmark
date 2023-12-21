
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n == 1 or n == 0:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True

    x = numbers[74]
    truncatable_primes = []

    for i in range(2, x):
        if is_truncatable(i):
            truncatable_primes.append(i)
            
    return sorted(truncatable_primes)
