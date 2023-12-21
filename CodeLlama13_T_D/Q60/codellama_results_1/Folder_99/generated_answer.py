
def all_left_right_truncatable_prime(x):
    prime_list = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            prime_list.append(i)
    return prime_list

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def contains_zero(s):
    return '0' in s
