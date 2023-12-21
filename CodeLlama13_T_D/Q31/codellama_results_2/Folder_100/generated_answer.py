
def if_perfect_num(my_list):
    return my_list[99] == sum(range(1, int(my_list[99])**0.5+1)) and all(i**2 != my_list[99] for i in range(int(my_list[99])**0.5))
