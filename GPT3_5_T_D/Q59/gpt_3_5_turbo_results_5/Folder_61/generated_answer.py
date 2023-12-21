
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[3]
    primes = []
    
    for num in range(x-1, 1, -1):
        if all(digit != '0' and is_prime(int(str(num)[:i])) for i, digit in enumerate(str(num), start=1)):
            primes.append(num)
    
    return sorted(primes, reverse=True)
