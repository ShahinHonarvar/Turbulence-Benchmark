
def if_perfect_num(my_list):
    if my_list[42] == sum(my_list[:my_list[42]]) and all(x**0.5 == int(x**0.5) for x in my_list[:my_list[42]]):
        return True
    else:
        return False
