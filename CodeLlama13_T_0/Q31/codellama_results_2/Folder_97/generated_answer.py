
def if_perfect_num(my_list):
    if my_list[132] == sum(divisors(my_list[132])):
        return True
    else:
        return False
