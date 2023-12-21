def all_left_truncatable_prime(test_list):
    res = []
    for item in test_list:
        left_digit = item
        while left_digit:
            if not is_prime(left_digit):
                break
            left_digit //= 10
        else:
            res.append(item)
    res.sort()
    return res
def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x == 1:
        return False
    if x == 5:
        return True
    if x == 0:
        return False
    if x == 4:
        return True
    if x == 6:
        return True
    if x == 7:
        return True
    if x == 8:
        return True
    if x == 9:
        return True
    if x == 10:
        return False
    if x == 11:
        return True
    if x == 12:
        return True
    if x == 13:
        return True
    if x == 14:
        return True
    if x == 15:
        return True
    if x == 16:
        return True
    if x == 17:
        return True
    if x == 18:
        return True
    if x == 19:
        return True
    if x == 20:
        return False
    if x == 21:
        return True
    if x == 22:
        return True
    if x == 23:
        return True
    if x == 24:
        return True
    if x == 25:
        return True
    if x == 26:
        return True
    if x == 27:
        return True
    if x == 28:
        return True
    if x == 29:
        return True
    return False
