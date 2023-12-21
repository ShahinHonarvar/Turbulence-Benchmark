
def all_left_truncatable_prime(t):
    x = t[89]
    primes = [2]
    left_truncatable_primes = []
    for possible_prime in range(3, x+1, 2):
        is_prime = True
        for num in range(2, int(possible_prime ** 0.5)+1):
            if possible_prime % num == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(possible_prime)

    for prime in primes:
        if '0' in str(prime):
            continue
        temp_prime = str(prime)
        left_truncatable = True
        while temp_prime != '':
            if int(temp_prime) not in primes:
                left_truncatable = False
                break
            temp_prime = temp_prime[1:]
        if left_truncatable:
            left_truncatable_primes.append(prime)

    return sorted(left_truncatable_primes, reverse=True)
