
def if_perfect_num(my_list):
    return my_list[222] in [x for x in range(1, int(my_list[222]**0.5) + 1) if my_list[222] % x == 0 and x > 1]
