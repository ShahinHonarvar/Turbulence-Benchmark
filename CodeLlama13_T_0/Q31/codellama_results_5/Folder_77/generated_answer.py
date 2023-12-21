
def if_perfect_num(my_list):
    if my_list[985] == sum(divisors(my_list[985])):
        return True
    else:
        return False
