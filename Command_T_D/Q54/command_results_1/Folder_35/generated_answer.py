def all_right_truncatable_prime(n):
    return [i for i in range(2, n[0] + 1) if is_right_truncatable_prime(i)]
def is_right_truncatable_prime(n):
    x = n
    while x > 1:
        if x % 2 == 0:
            return False
        x //= 2
    return True
