
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[96]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            prime_numbers.append(i)
    
    return sorted(prime_numbers, reverse=True)

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def contains_zero(s):
    return '0' in s
