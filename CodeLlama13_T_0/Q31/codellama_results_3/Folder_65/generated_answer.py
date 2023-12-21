
def if_perfect_num(my_list):
    if my_list[35] == sum(divisors(my_list[35])):
        return True
    else:
        return False
