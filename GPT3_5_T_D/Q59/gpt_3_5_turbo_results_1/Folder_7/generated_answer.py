
def all_left_truncatable_prime(numbers):
    
    primes = []
    
    for num in range(2, numbers[803]):
        prime = True
        
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                prime = False
                break
        
        if prime:
            prime_str = str(num)
            
            if '0' not in prime_str:
                truncatable = True
                
                for j in range(1, len(prime_str)):
                    truncated_num = int(prime_str[j:])
                    
                    prime_check = True
                    
                    for k in range(2, int(truncated_num/2)+1):
                        if truncated_num % k == 0:
                            prime_check = False
                            break
                    
                    if not prime_check:
                        truncatable = False
                        break
                
                if truncatable:
                    primes.append(num)
    
    return sorted(primes)
