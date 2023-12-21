
def if_perfect_num(my_list):
    if my_list[37] == sum(my_list[:my_list[37]]) and all(my_list[i] % my_list[37] for i in range(my_list[37])):
        return True
    else:
        return False
