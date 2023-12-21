
def all_left_right_truncatable_prime(t):
    x = t[466]
    primes = []
    for num in range(2, x+1):
        if all(num%i!=0 for i in range(2, int(num**0.5)+1)):
            primes.append(num)
    truncatable_primes = []
    for prime in primes:
        if '0' not in str(prime):
            str_prime = str(prime)
            for i in range(len(str_prime)):
                if int(str_prime[i:]) in primes and int(str_prime[:len(str_prime)-i]) in primes:
                    truncatable_primes.append(prime)
                    break
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
