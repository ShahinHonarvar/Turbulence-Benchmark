
def all_left_truncatable_prime(tuple):
    x = tuple[29]
    prime_list = []
    
    for i in range(1,x):
        if is_prime(i) and '0' not in str(i):
            prime_list.append(i)
            
    return sorted(prime_list, reverse=True)
