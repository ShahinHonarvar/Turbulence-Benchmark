
def all_left_right_truncatable_prime(n):
    return [i for i in range(2, n[0] + 1) if is_left_right_truncatable_prime(i)]

def is_left_right_truncatable_prime(n):
    if n <= 9:
        return True
    if n <= 99:
        return n % 10 >= 5
    if n <= 999:
        return n % 100 >= 5
    if n <= 9999:
        return n % 1000 >= 5
    if n <= 99999:
        return n % 10000 >= 5
    return False
