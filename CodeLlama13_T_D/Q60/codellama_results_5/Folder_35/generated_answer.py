
def all_left_right_truncatable_prime(x):
    lst = []
    for i in range(2, x+1):
        if is_prime(i) and not '0' in str(i):
            lst.append(i)
    return lst

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
