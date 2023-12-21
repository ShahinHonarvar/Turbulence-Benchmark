
import itertools

def all_left_right_truncatable_prime(n):
    z = list(range(2, n + 1))
    for num in z:
        i = str(num)
        l = len(i)
        while l > 2:
            i = i[1:l - 1] + i[-2:]
            l = len(i)
            if i in range(10, 100) and str(int(i)) == i:
                yield int(i)

def __starting_point():
    return list(sorted(list(all_left_right_truncatable_prime((10**5,)))))
