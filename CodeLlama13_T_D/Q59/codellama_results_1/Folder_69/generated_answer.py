
def all_left_truncatable_prime(tuple_of_ints):
    x = tuple_of_ints[760]
    prime_numbers = []
    
    for i in range(1, 9999983):
        if is_left_truncatable_prime(i):
            prime_numbers.append(i)
            
    return sorted(prime_numbers, reverse=True)
