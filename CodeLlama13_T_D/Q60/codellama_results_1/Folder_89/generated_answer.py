
def all_left_right_truncatable_prime(x):
    left_truncatable_primes = []
    for i in range(10, x+1):
        if is_prime(i) and not '0' in str(i):
            left_truncatable_primes.append(i)
    right_truncatable_primes = []
    for j in range(10, x+1):
        if is_prime(j) and not '0' in str(j):
            right_truncatable_primes.append(j)
    left_and_right_truncatable_primes = []
    for k in range(len(left_truncatable_primes)):
        if left_truncatable_primes[k] in right_truncatable_primes:
            left_and_right_truncatable_primes.append(left_truncatable_primes[k])
    return sorted(left_and_right_truncatable_primes, reverse=True)
