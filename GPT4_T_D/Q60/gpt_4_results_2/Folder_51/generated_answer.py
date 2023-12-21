
def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[54]
    primes = []
    for number in range(2,x+1):
        if all(number % i != 0 for i in range(2, number)):
            primes.append(number)
    truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        if '0' not in str_prime:
            condition = [all(int(str_prime[n:i]) % j !=0 for j in range(2, int(str_prime[n:i]))) for n in range(len(str_prime)) for i in range(n+1, len(str_prime)+1)]
            if all(condition):
                truncatable_primes.append(prime)
    return sorted(truncatable_primes)
