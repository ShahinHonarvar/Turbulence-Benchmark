
def all_left_right_truncatable_prime(args):
    return sorted(list(filter(left_right_truncatable_prime, range(1, args[0] + 1))), reverse=True)

def left_right_truncatable_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
