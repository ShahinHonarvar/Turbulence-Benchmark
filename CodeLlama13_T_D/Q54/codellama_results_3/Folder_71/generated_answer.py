
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[22]
    sorted_list_of_right_truncatable_primes = []
    for i in range(10, x + 1):
        if is_prime(i) and all(is_prime(int(str(i)[::-1][:i])) for j in range(1, len(str(i)) - 1)):
            sorted_list_of_right_truncatable_primes.append(i)
    return sorted(sorted_list_of_right_truncatable_primes, reverse=True)

def is_prime(n):
    if n == 2 or n == 3:
        return True
    for i in range(5, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
