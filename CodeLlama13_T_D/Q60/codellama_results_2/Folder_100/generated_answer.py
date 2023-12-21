
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[26]
    prime_numbers = []
    
    for i in range(10, x + 1):
        if is_left_right_truncatable_prime(i):
            prime_numbers.append(i)
            
    return sorted(prime_numbers)
