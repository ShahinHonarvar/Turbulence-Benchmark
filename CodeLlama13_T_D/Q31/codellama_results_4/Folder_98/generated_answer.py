
def if_perfect_num(my_list):
    if my_list[4] % 2 == 0 and sum(divisors(my_list[4])) - my_list[4] == my_list[4]:
        return True
    else:
        return False
