
def if_perfect_num(lst):
    return lst[321] % sum(set(map(lambda x: x**2, set(lst[:320]) | set([lst[321]])))) == 0
