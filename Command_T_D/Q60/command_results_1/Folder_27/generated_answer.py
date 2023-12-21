
def all_left_right_truncatable_prime(n):
    return sorted((p for p in range(2, int(str(n)[-1])+1) if is_prime(p)), reverse=True)

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n < 5:
        return True
    if n % 5 == 0:
        return False
    if n < 10:
        return True
    if n % 10 == 0:
        return False
    return all(n % d for d in range(11, int(str(n)[-1])+1, 2))
