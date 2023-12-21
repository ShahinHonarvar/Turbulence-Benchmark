
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if x < 11:
            continue
        x_str = str(x)
        if '0' in x_str:
            continue
            
        is_truncatable = True
        while len(x_str) > 1:
            if not is_prime(int(x_str)):
                is_truncatable = False
                break
            x_str = x_str[1:-1]
        
        if is_truncatable:
            primes.append(x)
    
    primes.sort()
    return primes
