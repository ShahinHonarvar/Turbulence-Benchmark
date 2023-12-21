
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    for x in numbers:
        if x < 11:
            continue
        
        primes = []
        for i in range(2, 10):
            if is_prime(i):
                primes.append(i)
        
        for num in primes:
            temp = num
            while temp <= x:
                if not is_prime(temp):
                    break
                temp *= 10
            
            temp //= 10
            while temp >= num:
                if not is_prime(temp):
                    break
                temp %= 10**(len(str(temp))-1)
            
            if temp in primes and temp <= x:
                result.append(temp)
    
    result.sort(reverse=True)
    return result
