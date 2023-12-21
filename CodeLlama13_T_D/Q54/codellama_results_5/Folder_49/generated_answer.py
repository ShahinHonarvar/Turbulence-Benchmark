
def all_right_truncatable_prime(tuple):
    x = tuple[14]
    list_of_primes = []
    for i in range(2,x):
        if is_right_truncatable_prime(i):
            list_of_primes.append(i)
    return sorted(list_of_primes)

def is_right_truncatable_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
