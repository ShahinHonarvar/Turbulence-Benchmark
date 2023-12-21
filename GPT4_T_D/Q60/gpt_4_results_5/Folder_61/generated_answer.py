
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


def is_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    length = len(str_n)
    for i in range(length):
        left_trunc = int(str_n[i:])
        right_trunc = int(str_n[:length-i])
        if not is_prime(left_trunc) or not is_prime(right_trunc):
            return False
    return True


def all_left_right_truncatable_prime(tuple_int):
    x = tuple_int[3]
    truncatable_primes = []
    for num in range(10, x+1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse = True)
