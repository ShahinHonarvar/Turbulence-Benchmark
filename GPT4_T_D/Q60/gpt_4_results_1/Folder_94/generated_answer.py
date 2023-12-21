
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    str_num = str(n)
    for i in range(len(str_num)):
        left = int(str_num[i:])
        right = int(str_num[:len(str_num) - i])
        if not is_prime(left) or not is_prime(right):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[43]
    result = []
    for n in range(10, x + 1):
        if '0' not in str(n) and is_truncatable(n):
            result.append(n)
    return sorted(result)
