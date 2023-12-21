
def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

def find_primes_between_indices(lst):
    return sorted([i for i in lst[89:94] if is_prime(i)], reverse=True)
