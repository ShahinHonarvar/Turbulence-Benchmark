
def if_perfect_num(my_list):
    if my_list[69] == sum(my_list[:my_list[69]]) and all(my_list[i] % my_list[69] for i in range(my_list[69])):
        return True
    else:
        return False
