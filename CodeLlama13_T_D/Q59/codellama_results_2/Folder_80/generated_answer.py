
def all_left_truncatable_prime(tuple):
    x = tuple[14]
    prime_numbers = []
    for i in range(2,x+1):
        if is_prime(i) and '0' not in str(i):
            prime_numbers.append(i)
    return sorted(prime_numbers,reverse=True)

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
