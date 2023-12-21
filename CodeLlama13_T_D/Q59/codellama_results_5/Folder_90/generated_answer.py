
def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[466]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and str(i).find("0") == -1:
            prime_numbers.append(i)
    left_truncatable_primes = []
    for p in prime_numbers:
        left_truncatable = True
        for i in range(2, int(len(str(p))/2)+1):
            if not is_prime(int(str(p)[:i])):
                left_truncatable = False
                break
        if left_truncatable:
            left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes, reverse=True)
