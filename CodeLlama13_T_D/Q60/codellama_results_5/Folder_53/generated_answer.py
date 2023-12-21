
def all_left_right_truncatable_prime(x):
    return sorted([i for i in range(2, x+1) if is_prime(i) and is_left_right_truncatable_prime(i)], reverse=True)

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    s = str(n)
    for i in range(len(s)):
        if '0' in s[i+1:] or not is_prime(int(s[i:])):
            return False
    return True
