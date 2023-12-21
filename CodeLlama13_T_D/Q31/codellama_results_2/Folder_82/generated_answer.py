
def if_perfect_num(my_list):
    if my_list[83] == sum(divisors(my_list[83])):
        return True
    else:
        return False
