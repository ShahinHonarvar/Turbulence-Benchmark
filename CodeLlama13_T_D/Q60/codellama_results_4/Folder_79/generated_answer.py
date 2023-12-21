
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[91]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_numbers.append(i)
    left_right_truncatable_primes = []
    for i in prime_numbers:
        str_i = str(i)
        if not str_i[0] == '0' and not str_i[-1] == '0':
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
