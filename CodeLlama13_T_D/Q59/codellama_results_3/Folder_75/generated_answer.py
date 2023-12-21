
def all_left_truncatable_prime(numbers):
    x = numbers[41]
    prime_list = []
    
    for i in range(2, x+1):
        if is_prime(i) and not any(str(i).startswith('0') for i in str(i)):
            prime_list.append(i)
            
    return sorted(prime_list)
    
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
