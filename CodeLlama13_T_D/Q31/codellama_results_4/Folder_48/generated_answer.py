
def if_perfect_num(my_list):
    if my_list[247] == sum(filter(lambda x: x != 0 and x % my_list[247] == 0, range(1, int(my_list[247])))):
        return True
    else:
        return False
