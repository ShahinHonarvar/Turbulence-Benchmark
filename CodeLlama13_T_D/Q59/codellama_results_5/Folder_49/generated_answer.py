
def all_left_truncatable_prime(numbers):
    x = numbers[14]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not '0' in str(i):
            primes.append(i)
    
    for j in range(len(primes)):
        for k in range(j+1, len(primes)):
            if str(primes[j]) in str(primes[k]):
                primes.remove(primes[j])
                break
            
    return sorted(primes)
