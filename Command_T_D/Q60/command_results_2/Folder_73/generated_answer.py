
def all_left_right_truncatable_prime(a):
    x = a[97]
    l = []
    for i in range(2, int(str(x)[0]) + 1):
        if str(i) not in str(x):
            for j in range(2, int(str(x)[-1]) + 1):
                if str(i) + str(j) not in str(x):
                    l.append(i * 10 ** j)
                    break
    return l
