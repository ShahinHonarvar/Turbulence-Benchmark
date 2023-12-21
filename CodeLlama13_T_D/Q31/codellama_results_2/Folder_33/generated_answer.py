
def if_perfect_num(my_list):
    return my_list[321] % 6 == 0 and sum(set(my_list[:321])) == my_list[321]
