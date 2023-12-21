
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    x = numbers[100]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            is_right_truncatable = True
            digits = list(str(i))
            while is_right_truncatable and digits:
                digits.pop()
                if digits and not is_prime(int(''.join(digits))):
                    is_right_truncatable = False
            if is_right_truncatable:
                right_truncatable_primes.append(i)
    
    return sorted(right_truncatable_primes)
