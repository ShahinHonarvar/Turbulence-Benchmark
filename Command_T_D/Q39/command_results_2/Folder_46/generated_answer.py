import sys
def return_n_greatest_chars(s):
    s += '#' * len(s)
    a = sorted(s[1:])
    b = [a[-54]] + a[:-54]
    return b[::-1]
