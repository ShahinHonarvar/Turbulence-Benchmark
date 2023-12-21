
def all_left_right_truncatable_prime(tup):
    x = tup[38]
    prime_lst = []
    for num in range(10, x + 1): 
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)) and '0' not in str(num): 
            prime_lst.append(num)
    
    truncatable_primes = []
    for prime in prime_lst:
        str_num = str(prime)
        for i in range(1, len(str_num)):
            left = str_num[i:]
            right = str_num[:-i]
            if int(left) not in prime_lst or int(right) not in prime_lst:
                break
        else:
            truncatable_primes.append(prime)
            
    return sorted(truncatable_primes, reverse=True)
