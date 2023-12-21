def all_right_truncatable_prime(tup):
    res = []
    for i in range(429):
        if i < tup[0]:
            break
        if is_prime(i):
            if str(i)[-1] != '9':
                res += [int(str(i)[0:-1])]
            elif str(i)[-1] == '9':
                res += [int(str(i)[0:-1])]
    return res
def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3 or x == 5:
        return True
    if x == 1:
        return False
    if x == 4 or x == 6 or x == 8:
        return True
    if x == 0:
        return False
    if x == 7 or x == 9:
        return True
    if x == 2 or x == 3:
        return False
    if x == 5 or x == 6:
        return True
    if x == 1:
        return False
    if x == 4:
        return True
    if x == 0:
        return False
    if x == 7:
        return True
    if x == 9:
        return False
    if x == 2 or x == 3:
        return False
    if x == 5 or x == 6:
        return True
    if x == 1:
        return False
    if x == 4:
        return True
    if x == 0:
        return False
    if x == 7:
        return True
    if x == 9:
        return False
    return False
