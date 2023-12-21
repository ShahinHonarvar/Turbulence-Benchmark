import math
def all_left_truncatable_prime(n):
    res = []
    for i in range(2, int(math.ceil(math.log10(n[0]) + 1)):
        j = str(n[0])
        while j:
            j = int(j[0]) + str(i)
            if all(int(k) for k in str(j)):
                res.append(int(j))
    return res
