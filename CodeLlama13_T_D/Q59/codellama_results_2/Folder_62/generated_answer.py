
def all_left_truncatable_prime(my_tuple):
    x = my_tuple[70]
    prime_list = []
    
    for i in range(2, x+1):
        if is_prime(i) and not any(map(lambda j: '0' in str(j), [i]*len(str(i)))):
            prime_list.append(i)
            
    return sorted(prime_list)
