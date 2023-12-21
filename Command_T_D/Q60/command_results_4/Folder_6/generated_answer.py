
def all_left_right_truncatable_prime(x):
    res = []
    for i in range(2, x // 2 + 1):
        if is_left_right_truncatable_prime(i):
            res.append(i)
    for i in range(x // 2, x // 3 + 1):
        if is_left_right_truncatable_prime(i):
            res.append(i)
    return res

def is_left_right_truncatable_prime(x):
    x = str(x)
    if x[0] == '0':
        return False
    if len(x) == 1:
        return True
    if x[0] == '1':
        return False
    if x[0] == '2':
        return True
    if x[0] == '3':
        return False
    if x[0] == '4':
        return True
    if x[0] == '5':
        return False
    if x[0] == '6':
        return True
    if x[0] == '7':
        return False
    if x[0] == '8':
        return True
    if x[0] == '9':
        return False
    if x[0] == '0' or x[0] == '1':
        return False
    if x[0] == '2' or x[0] == '3':
        return True
    if x[0] == '4' or x[0] == '5':
        return False
    if x[0] == '6' or x[0] == '7':
        return True
    if x[0] == '8' or x[0] == '9':
        return False
    if x[0] == '0' or x[0] == '1' or x[0] == '2' or x[0] == '3':
        return False
    if x[0] == '4' or x[0] == '5' or x[0] == '6' or x[0] == '7':
        return True
    if x[0] == '8' or x[0] == '9' or x[0] == '0' or x[0] == '1' or x[0] == '2' or x[0] == '3':
        return False
    if x[0] == '4' or x[0] == '5' or x[0] == '6' or x[0] == '7' or x[0] == '8' or x[0] == '9':
        return True
    return False
