
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        trunc_num = int(str_n[i:])
        if not is_prime(trunc_num):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[645]
    result = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result)
