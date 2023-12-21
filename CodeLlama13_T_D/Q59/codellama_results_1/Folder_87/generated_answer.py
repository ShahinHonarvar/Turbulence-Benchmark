
def all_left_truncatable_prime(tuple_of_positive_integers):
    left_truncatable_primes = []
    for number in tuple_of_positive_integers:
        if is_left_truncatable_prime(number):
            left_truncatable_primes.append(number)
    return sorted(left_truncatable_primes, reverse=True)

def is_left_truncatable_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True
