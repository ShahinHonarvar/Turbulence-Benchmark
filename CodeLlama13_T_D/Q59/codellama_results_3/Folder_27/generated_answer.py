
def all_left_truncatable_prime(x):
    left_truncatable_primes = []
    for i in range(10**7, x+1):
        if str(i).find('0') == -1:
            is_prime = True
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)
