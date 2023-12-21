def all_left_truncatable_prime(x_tuple):
    res = []
    for x in range(88, x_tuple[0], 1):
        for i in range(10):
            temp = str(x)
            while temp[i] == '0':
                temp = temp[:i] + temp[i + 1 :]
            if temp == '':
                break
            if is_prime(int(temp)):
                res.append(int(temp))
    return res
def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    maxDivisor = int(x ** .5) + 1
    for i in range(5, maxDivisor, 6):
        if x % i == 0:
            return False
    return True
