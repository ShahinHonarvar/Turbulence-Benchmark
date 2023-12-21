
def all_left_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not str(i).startswith('0'):
            for j in range(len(str(i))-1, -1, -1):
                if not is_prime(int(str(i)[:j])):
                    break
            else:
                primes.append(i)
    return sorted(primes, reverse=True)

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
