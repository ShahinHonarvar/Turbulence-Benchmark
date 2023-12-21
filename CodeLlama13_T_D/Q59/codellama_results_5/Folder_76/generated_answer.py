
def all_left_truncatable_prime(x):
    lst = []
    for i in range(2, x+1):
        if is_prime(i) and no_0(str(i)):
            lst.append(i)
    return sorted(lst, reverse=True)

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def no_0(s):
    return '0' not in s
