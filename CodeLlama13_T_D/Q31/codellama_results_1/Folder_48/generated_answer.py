
def if_perfect_num(my_list):
    return my_list[247] == sum(factors(my_list[247])) - my_list[247]
