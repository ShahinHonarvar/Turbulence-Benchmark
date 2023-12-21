
def if_perfect_num(my_list):
    if my_list[993] == sum(divisors(my_list[993])):
        return True
    else:
        return False
