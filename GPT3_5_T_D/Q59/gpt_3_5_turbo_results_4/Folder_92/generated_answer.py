
def all_left_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    x = numbers[7]
    left_truncatable_primes = []
    
    for i in range(2, x):
        if '0' in str(i):
            continue
        if is_prime(i):
            truncatable = True
            num = str(i)
            while len(num) > 1:
                num = num[1:]
                if not is_prime(int(num)):
                    truncatable = False
                    break
            if truncatable:
                left_truncatable_primes.append(i)
    
    return sorted(left_truncatable_primes)
