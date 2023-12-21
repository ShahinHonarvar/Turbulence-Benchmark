
def all_left_right_truncatable_prime(n):
    res = []
    for i in range(2, n[0] + 1):
        x = str(i)
        while x[0] == "0":
            x = x[1:]
        while x[-1] == "0":
            x = x[:-1]
        if x == "1" or x == "2":
            res.append(i)
        elif all(y == "0" for y in x):
            res.append(i)
    return res
