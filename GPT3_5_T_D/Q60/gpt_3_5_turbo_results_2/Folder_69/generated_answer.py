
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
        
        left = str(num)
        right = str(num)
        
        while len(left) > 2:
            left = left[1:]
            right = right[:-1]
            
            if not is_prime(int(left)) or not is_prime(int(right)):
                return False
        
        return True
        
    x = numbers[760]
    primes = [num for num in range(2, x + 1) if is_prime(num) and is_truncatable_prime(num)]
    return sorted(primes, reverse=True)
