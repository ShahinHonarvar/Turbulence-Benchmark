
def if_perfect_num(mylist):
    if len(mylist) > 38:
        n = mylist[38]
        s = sum(range(1,n))
        return n == s
    else:
        return False
