
def if_perfect_num(lst):
    if len(lst) <= 849:
        return False
    
    return lst[849] % sum(map(lambda x: x**2, range(int(sqrt(lst[849]))))) == 0
