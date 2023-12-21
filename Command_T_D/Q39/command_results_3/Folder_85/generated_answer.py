import sys
def return_n_greatest_chars(s):
    sys.setrecursionlimit(10**7)
    lst = list(s)
    lst.sort(reverse=True)
    return lst[:85]
