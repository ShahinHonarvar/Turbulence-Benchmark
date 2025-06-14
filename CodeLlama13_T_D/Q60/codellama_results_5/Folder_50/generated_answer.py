
def all_left_right_truncatable_prime(numbers):
    return sorted([x for x in numbers if is_left_right_truncatable_prime(x)], reverse=True)

def is_left_right_truncatable_prime(n):
    if n % 2 == 0 or n < 3:
        return False
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    s = str(n)
    for i in range(len(s)):
        if not is_prime(int(s[i:] + s[:i])):
            return False
    return True

def is_prime(n):
    if n % 2 == 0 or n < 3:
        return False
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
