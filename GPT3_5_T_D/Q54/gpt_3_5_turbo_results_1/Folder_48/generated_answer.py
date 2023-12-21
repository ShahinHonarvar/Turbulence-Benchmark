
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[835]
    prime_numbers = []
    
    for n in range(2, x):
        if is_prime(n):
            truncatable = True
            num = str(n)
            
            while num and truncatable:
                if not is_prime(int(num)):
                    truncatable = False
                num = num[:-1]
            
            if truncatable:
                prime_numbers.append(n)
    
    return sorted(prime_numbers)
