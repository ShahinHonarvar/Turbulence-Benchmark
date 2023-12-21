
def all_left_right_truncatable_prime(t):
    x = t[88]
    primes = []
    for num in range(2, x+1):
        if all(num%i!=0 for i in range(2, int(num**0.5)+1)):
            primes.append(num)
    truncatable_primes = []
    for prime in primes:
        if '0' not in str(prime):
            str_prime = str(prime)
            truncatable = True
            for i in range(len(str_prime)):
                if int(str_prime[i:]) not in primes or int(str_prime[:len(str_prime)-i]) not in primes:
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(prime)
    return sorted(truncatable_primes)
