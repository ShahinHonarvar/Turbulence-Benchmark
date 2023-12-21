
def all_left_right_truncatable_prime(x):
    left_truncatable = []
    for i in range(2, x+1):
        if is_left_truncatable_prime(i):
            left_truncatable.append(i)

    right_truncatable = []
    for j in reversed(range(x)):
        if is_right_truncatable_prime(j+1):
            right_truncatable.append(j+1)

    return list(set(left_truncatable + right_truncatable))

def is_left_truncatable_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True
