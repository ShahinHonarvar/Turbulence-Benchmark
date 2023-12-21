import re
def all_right_truncatable_prime(test_tup):
    res = []
    for i in range(1, int(test_tup[37])+1):
        j = str(i)
        while not re.match(r'^[1-9][0-9]*$', j):
            j = j[:-1]
        if all(int(d) for d in j):
            res.append(i)
    return res
