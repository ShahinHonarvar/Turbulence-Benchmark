
def all_left_right_truncatable_prime(tup):
    x = tup[91]
    primes = []
    for num in range(2, x+1):
        if all(num%i!=0 for i in range(2, int(num**0.5)+1)):
            primes.append(num)
    truncatable_primes = []
    for prime in primes:
        if '0' in str(prime):
            continue
        str_prime = str(prime)
        left_right_truncatable = True
        for i in range(len(str_prime)):
            left_truncated = int(str_prime[i:])
            right_truncated = int(str_prime[:len(str_prime)-i])
            if left_truncated not in primes or right_truncated not in primes:
                left_right_truncatable = False
                break
        if left_right_truncatable:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)
