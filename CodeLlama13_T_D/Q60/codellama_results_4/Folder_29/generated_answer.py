
def all_left_right_truncatable_prime(x):
    left_trunc = []
    right_trunc = []
    for i in range(2, x+1):
        if is_prime(i):
            left_trunc.append(i)
            right_trunc.append(i)
        else:
            continue
    return [left*right for left in left_trunc for right in right_trunc if str(left*right)[1:-1] == '0' and is_prime(left*right)]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
