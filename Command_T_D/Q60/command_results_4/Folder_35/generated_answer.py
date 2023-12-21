
def all_left_right_truncatable_prime(n):
    return sorted(list(filter(lambda x: x < n[0] or x == n[0] and x <= n[1] and is_left_right_truncatable_prime(x), range(2, n[1] + 1))))

def is_left_right_truncatable_prime(x):
    x = str(x)
    while len(x) > 2:
        if x[0] == '0' or x[-1] == '0':
            return False
        if x[0] == '1' and x[1] == '0':
            return False
        if x[-1] == '1' and x[-2] == '0':
            return False
        x = int(x[1:-1])
    return True
