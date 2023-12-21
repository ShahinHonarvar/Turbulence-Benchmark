
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[760]
    left_and_right_truncatable_primes = []
    for i in range(2, x+1):
        if is_prime(i) and no_zeroes(str(i)):
            left_and_right_truncatable_primes.append(i)
    return sorted(left_and_right_truncatable_primes, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def no_zeroes(s):
    return not '0' in s
