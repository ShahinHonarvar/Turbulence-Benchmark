
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[71]
    truncatable_primes = []
    
    for num in range(10, x + 1):
        if num % 10 != 0 and is_prime(num):
            num_str = str(num)
            
            is_truncatable = True
            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:i])):
                    is_truncatable = False
                    break
            
            if is_truncatable:
                truncatable_primes.append(num)
    
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
