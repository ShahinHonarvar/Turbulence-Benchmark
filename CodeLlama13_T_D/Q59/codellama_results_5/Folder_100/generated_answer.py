
def all_left_truncatable_prime(tuple):
    return sorted([x for x in range(2, tuple[26]) if is_left_truncatable_prime(x)])

def is_left_truncatable_prime(num):
    str_num = str(num)
    for i in range(len(str_num)):
        if '0' in str_num[:i]: return False
        if not is_prime(int(str_num[:i])): return False
    return True

def is_prime(num):
    if num == 1 or num == 0: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True
