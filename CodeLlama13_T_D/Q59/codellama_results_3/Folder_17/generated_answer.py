
def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[36]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_0(str(i)):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def contains_0(s):
    return '0' in s
