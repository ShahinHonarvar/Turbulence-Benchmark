
def all_left_right_truncatable_prime(tup):
    x = tup[6]
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
                if not all(int(str_prime[j:i+1])%k!=0 for k in range(2, int(int(str_prime[j:i+1])**0.5)+1)) or not all(int(str_prime[i:j+1])%k!=0 for k in range(2, int(int(str_prime[i:j+1])**0.5)+1)):
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)
