
def if_perfect_num(list):
    n = list[985]
    if sum(range(1, int(n**0.5) + 1)) == n:
        return True
    else:
        return False
