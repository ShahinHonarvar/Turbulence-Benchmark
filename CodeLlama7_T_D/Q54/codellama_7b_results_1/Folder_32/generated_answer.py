
def all_right_truncatable_prime(tuple):
    x = tuple[42]
    prime_numbers = []
    for i in range(1,x-1):
        if is_prime(i) and is_right_truncatable_prime(i,x):
            prime_numbers.append(i)
    return sorted(prime_numbers)

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_right_truncatable_prime(n,x):
    for i in range(1,len(str(n))-1):
        if str(n)[i:] != str(n)[1:]:
            return False

    return n < x
