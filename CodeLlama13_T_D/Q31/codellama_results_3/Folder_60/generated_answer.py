
def if_perfect_num(my_list):
    if my_list[88] % 2 == 0 and sum(divisors(my_list[88])) - my_list[88] == my_list[88]:
        return True
    else:
        return False
