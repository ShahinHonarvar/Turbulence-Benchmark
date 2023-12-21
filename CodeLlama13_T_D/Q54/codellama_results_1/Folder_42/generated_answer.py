
def all_right_truncatable_prime(numbers):
    x = numbers[64]
    prime_list = []
    
    for i in range(2, x+1):
        if is_prime(i):
            prime_list.append(i)
            
    truncatable_prime_list = []
    
    for j in prime_list:
        if is_right_truncatable_prime(j):
            truncatable_prime_list.append(j)
            
    return sorted(truncatable_prime_list, reverse=True)
