
def all_left_right_truncatable_prime(tup):
    return sorted(set(filter(left_right_truncatable_prime, range(tup[126] + 1))), reverse=True)

def left_right_truncatable_prime(x):
    if x <= 1:
        return True
    elif x <= 3:
        return x == 2 or x == 3
    elif x <= 99:
        return x == 5 or x == 7 or x == 11 or x == 13 or x == 17 or x == 19 or x == 23 or x == 29 or x == 31 or x == 37 or x == 41 or x == 43 or x == 47 or x == 53 or x == 59 or x == 61 or x == 67 or x == 71 or x == 73 or x == 79 or x == 83 or x == 89 or x == 97
    elif x <= 999:
        return x == 101 or x == 103 or x == 107 or x == 109 or x == 113 or x == 127 or x == 521 or x == 607 or x == 1279 or x == 2203 or x == 2281 or x == 3217 or x == 4253 or x == 4423 or x == 9689 or x == 9967
