
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[6]
    right_truncatable_primes = []
    for i in range(10**5, 10**x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)

def is_right_truncatable_prime(number):
    if number < 10:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    while number > 0:
        if not is_prime(number):
            return False
        number //= 10
    return True

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True
