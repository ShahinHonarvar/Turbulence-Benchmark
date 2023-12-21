
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[31]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and has_no_zero(str(i)):
            prime_numbers.append(i)
    
    truncatable_prime_numbers = []
    for i in prime_numbers:
        if is_left_and_right_truncatable_prime(i):
            truncatable_prime_numbers.append(i)
    
    return sorted(truncatable_prime_numbers, reverse=True)
