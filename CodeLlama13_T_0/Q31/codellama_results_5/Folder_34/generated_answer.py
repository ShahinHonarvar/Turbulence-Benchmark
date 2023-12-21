
def if_perfect_num(my_list):
    if my_list[97] == sum(divisors(my_list[97])):
        return True
    else:
        return False
