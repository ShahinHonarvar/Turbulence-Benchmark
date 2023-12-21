
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[792]
    truncatable_list = []
    for num in range(2, x):
        if left_truncatable(num):
            truncatable_list.append(num)
    return sorted(truncatable_list)
