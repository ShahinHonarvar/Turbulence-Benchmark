def all_right_truncatable_prime(test_tup):
    res = []
    for i in range(test_tup[0]):
        x = 10**i + 1
        if x == test_tup[0]:
            break
        while x > 1:
            if x % 2 == 0:
                x /= 2
            elif x % 3 == 0:
                x /= 3
            elif x % 5 == 0:
                x /= 5
            elif x % 7 == 0:
                x /= 7
            elif x % 11 == 0:
                x /= 11
            elif x % 13 == 0:
                x /= 13
            elif x % 17 == 0:
                x /= 17
            elif x % 19 == 0:
                x /= 19
            elif x % 23 == 0:
                x /= 23
            elif x % 29 == 0:
                x /= 29
            elif x % 31 == 0:
                x /= 31
            elif x % 37 == 0:
                x /= 37
            elif x % 41 == 0:
                x /= 41
            elif x % 43 == 0:
                x /= 43
            elif x % 47 == 0:
                x /= 47
            elif x % 53 == 0:
                x /= 53
            elif x % 59 == 0:
                x /= 59
            elif x % 61 == 0:
                x /= 61
            elif x % 67 == 0:
                x /= 67
            elif x % 71 == 0:
                x /= 71
            elif x % 73 == 0:
                x /= 73
            elif x % 79 == 0:
                x /= 79
            elif x % 83 == 0:
                x /= 83
            elif x % 89 == 0:
                x /= 89
            elif x % 97 == 0:
                x /= 97
            elif x % 101 == 0:
                x /= 101
            elif x % 103 == 0:
                x /= 103
            elif x % 107 == 0:
                x /= 107
            elif x % 109 == 0:
                x /= 109
            elif x % 113 == 0:
                x /= 113
            elif x % 127 == 0:
                x /= 127
            elif x % 521 == 0:
                x /= 521
            elif x % 607 == 0:
                x /= 607
            elif x % 1279 == 0:
                x /= 1279
            elif x % 2203 == 0:
                x /= 2203
            elif x % 2281 == 0:
                x /= 2281
            elif x % 3217 == 0:
                x /= 3217
            elif x % 4253 == 0:
                x /= 4253
            elif x % 4423 == 0:
                x /= 4423
            elif x % 9689 == 0:
                x /= 9689
            elif x % 11213 == 0:
                x /= 11213
            elif x % 19937 == 0:
                x /= 19937
            elif x % 21701 == 0:
                x /= 21701
            elif x % 23209 == 0:
                x /= 23209
            elif x % 44497 == 0:
                x /= 44497
            elif x % 110503 == 0:
                x /= 110503
            elif x % 199937 == 0:
                x /= 199937
            elif x % 219997 == 0:
                x /= 219997
            elif x % 300003 == 0:
                x /= 300003
            elif x % 400009 == 0:
                x /= 400009
            elif x % 900001 == 0:
                x /= 900001
            elif x % 990000 == 0:
                x /= 990000
            elif x % 999000 == 0:
                x /= 999000
            elif x % 999909 == 0:
                x /= 999909
            elif x % 996691 == 0:
                x /= 996691
            elif x % 9996693 == 0:
                x /= 9996693
            elif x % 9996699 == 0:
                x /= 9996699
            elif x % 999967 == 0:
                x /= 999967
            elif x % 999969 == 0:
                x /= 999969
            elif x % 999983 == 0:
                x /= 999983
            elif x % 999985 == 0:
                x /= 999985
            elif x % 999999 == 0:
                x /= 999999
            if isprime(x):
                res += [x]
    return res
