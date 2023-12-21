
def all_right_truncatable_prime(tuple):
    x = tuple[52]
    prime_list = []
    for i in range(1, x):
        if is_prime(i):
            prime_list.append(i)
    
    right_truncatable_prime_list = []
    for j in prime_list:
        if is_right_truncatable_prime(j):
            right_truncatable_prime_list.append(j)
    
    return sorted(right_truncatable_prime_list, reverse=True)
