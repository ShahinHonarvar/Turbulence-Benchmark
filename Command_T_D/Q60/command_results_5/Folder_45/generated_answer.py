
def all_left_right_truncatable_prime(x):
    res = []
    for num in range(2, x+1):
        if is_left_right_truncatable_prime(num):
            res.append(num)
    return res

def is_left_right_truncatable_prime(num):
    # does num contain 0?
    if str(num).count("0") > 1:
        return False
    # if not, return True
    # is it prime?
    if num <= 1:
        return True
    # if not, return False
    # does it remain prime if leftmost and rightmost digits are removed?
    if str(num).count("0") == 1:
        return False
    if str(num).count("0") == 0:
        return True
    return False
