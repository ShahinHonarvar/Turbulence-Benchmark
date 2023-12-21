
def if_perfect_num(lst):
    if lst[64] == sum(filter(lambda x: x % lst[64] == 0, range(1, lst[64]))):
        return True
    else:
        return False
