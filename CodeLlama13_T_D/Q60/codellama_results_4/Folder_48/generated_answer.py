
def all_left_right_truncatable_prime(tuple):
    lst = []
    for i in range(len(tuple)):
        if is_left_and_right_truncatable_prime(tuple[i]):
            lst.append(tuple[i])
    return sorted(lst)

def is_left_and_right_truncatable_prime(n):
    if n < 10:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
