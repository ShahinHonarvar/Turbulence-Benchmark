
def if_perfect_num(my_list):
    if len(my_list) > 6:
        return my_list[6] == sum(filter(lambda x: x <= my_list[6], range(1, my_list[6]+1)))
    else:
        return False
