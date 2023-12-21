
def all_left_right_truncatable_prime(x):
    lst = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            if left_and_right_truncatable(i):
                lst.append(i)
    return sorted(lst)

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def contains_zero(s):
    return '0' in s

def left_and_right_truncatable(n):
    while len(str(n)) > 2:
        if not is_prime(n):
            return False
        n = int(str(n)[:-1])
    return True
