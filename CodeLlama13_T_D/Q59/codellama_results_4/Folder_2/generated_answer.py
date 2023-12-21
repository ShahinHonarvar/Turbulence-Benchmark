
def all_left_truncatable_prime(numbers):
    x = numbers[618]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and no_zero(str(i)):
            prime_numbers.append(i)
    
    left_truncatable_prime_numbers = []
    for p in prime_numbers:
        if is_left_truncatable_prime(p):
            left_truncatable_prime_numbers.append(p)
            
    return sorted(left_truncatable_prime_numbers)

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def no_zero(s):
    return '0' not in s

def is_left_truncatable_prime(p):
    while p > 0:
        if not is_prime(int(str(p)[:1])):
            return False
        p = int(str(p)[1:])
    return True
