
def all_left_right_truncatable_prime(x):
    result = []
    for i in range(2, x+1):
        if is_prime(i) and is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if str(n).count('0') > 0:
        return False
    for i in range(len(str(n))-1, 0, -1):
        if not is_prime(int(str(n)[:i])):
            return False
    return True
