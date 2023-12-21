import sys
def all_right_truncatable_prime(arr):
    res = []
    for x in arr:
        if x > 2:
            x -= 1
            while x > 1:
                if all(d % 10 != d for d in str(x)):
                    res.append(x)
                    x -= 1
                x //= 10
    return res
