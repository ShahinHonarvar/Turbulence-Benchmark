
def all_left_right_truncatable_prime(x):
    prime_list = []
    for i in range(2, x+1):
        if is_prime(i) and not any(str(i).startswith('0') or str(i)[-1] == '0'):
            prime_list.append(i)
    
    return sorted(prime_list, reverse=True)
