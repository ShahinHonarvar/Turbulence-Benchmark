
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable(x):
    str_x = str(x)
    if '0' in str_x:
        return False
    for i in range(len(str_x)):
        if not is_prime(int(str_x[i:])) or not is_prime(int(str_x[:len(str_x) - i])):
            return False
    return True

def all_left_right_truncatable_prime(tuple_arg):
    x = tuple_arg[85]
    return sorted([i for i in range(10, x+1) if is_left_right_truncatable(i)])
