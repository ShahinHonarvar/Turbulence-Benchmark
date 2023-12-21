import sys
def all_right_truncatable_prime(n):
    x = int(n[835])
    # your code here
    res = []
    for i in range(2, x // 2 + 1):
        if is_right_truncatable_prime(i):
            res.append(i)
    return res
    
def is_right_truncatable_prime(n):
    # your code here
    for i in range(2, int(str(n)[-1]) + 1):
        if n % i == 0:
            return False
    return True
