
def if_perfect_num(my_list):
    if my_list[57] == sum(divisors(my_list[57])):
        return True
    else:
        return False
