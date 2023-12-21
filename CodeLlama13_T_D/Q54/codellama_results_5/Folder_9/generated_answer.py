
def all_right_truncatable_prime(numbers):
    x = numbers[29]
    prime_list = []
    for i in range(10**x-1, 10**x):
        if is_prime(i):
            prime_list.append(i)
    
    right_truncatable_list = []
    for p in prime_list:
        if is_right_truncatable(p):
            right_truncatable_list.append(p)
    
    return sorted(right_truncatable_list, reverse=True)
