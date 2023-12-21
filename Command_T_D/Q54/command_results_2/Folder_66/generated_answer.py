def all_right_truncatable_prime(test_list):
    res = []
    for x in range(2, int(test_list[25]) + 1):
        if is_prime(x):
            i = 0
            while i < len(str(x)):
                if str(x)[i] != '9':
                    break
                i += 1
            if x % 10 == 0:
                res.append(x)
    return res
def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x == 1 or x == 5:
        return False
    if x == 4 or x == 6:
        return True
    if x == 8 or x == 9:
        return False
    if x == 7 or x == 11:
        return True
    if x == 10 or x == 12:
        return False
    if x == 13 or x == 17:
        return True
    if x == 16 or x == 18:
        return False
    if x == 19 or x == 23:
        return True
    if x == 20 or x == 21:
        return False
    if x == 22 or x == 26:
        return True
    if x == 24 or x == 25:
        return False
    if x == 27:
        return True
