
def if_perfect_num(my_list):
    if my_list[56] == sum(divisors(my_list[56])):
        return True
    else:
        return False
