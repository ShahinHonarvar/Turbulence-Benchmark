
def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n**0.5)+1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[466]
    result = []

    for num in range(10, x+1):
        if '0' in str(num):
            continue
        is_truncatable = True
        for i in range(len(str(num))):
            left_trunc = int(str(num)[i:])
            right_trunc = int(str(num)[:len(str(num))-i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                is_truncatable = False
                break
        if is_truncatable:
            result.append(num)
    return sorted(result, reverse=True)
