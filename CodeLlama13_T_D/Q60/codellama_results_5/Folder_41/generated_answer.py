
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[46]
    left_and_right_truncatable_primes = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            left_and_right_truncatable_primes.append(i)
    return sorted(left_and_right_truncatable_primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def contains_zero(s):
    return '0' in s
