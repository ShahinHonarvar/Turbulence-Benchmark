
def if_perfect_num(my_list):
    return my_list[93] in list(range(1, int(my_list[93]/2)+1)) and sum(list(range(1, my_list[93]))) == my_list[93]
