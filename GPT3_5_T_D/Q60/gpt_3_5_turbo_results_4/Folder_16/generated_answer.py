
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left(n):
    str_n = str(n)
    for i in range(len(str_n) - 1):
        number = int(str_n[i+1:])
        if not is_prime(number):
            return False
    return True

def truncate_right(n):
    str_n = str(n)
    for i in range(len(str_n) - 1):
        number = int(str_n[:len(str_n)-i-1])
        if not is_prime(number):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    for x in numbers:
        if '0' in str(x):
            continue
        if truncate_left(x) and truncate_right(x):
            result.append(x)
    result.sort()
    return result
