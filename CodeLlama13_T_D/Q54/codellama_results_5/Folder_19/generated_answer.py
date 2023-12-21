
def all_right_truncatable_prime(x):
    prime_list = []
    for i in range(10**(x-1), x):
        if is_right_truncatable_prime(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)

def is_right_truncatable_prime(n):
    if n % 2 == 0 or n % 5 == 0:
        return False
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
