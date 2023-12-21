
def all_left_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    x = numbers[70]
    primes = []
    for i in range(2, x):
        if '0' not in str(i):
            truncatable = True
            for j in range(len(str(i))):
                if not is_prime(int(str(i)[j:])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    
    return sorted(primes)
