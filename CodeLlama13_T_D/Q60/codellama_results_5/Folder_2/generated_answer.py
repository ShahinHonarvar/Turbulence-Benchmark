
def all_left_right_truncatable_prime(tuple):
    x = tuple[618]
    prime_list = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            prime_list.append(i)
    
    left_right_truncatable_prime_list = []
    for i in prime_list:
        if is_left_and_right_truncatable_prime(i):
            left_right_truncatable_prime_list.append(i)
    
    return sorted(left_right_truncatable_prime_list)
