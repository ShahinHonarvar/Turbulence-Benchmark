
def if_perfect_num(my_list):
    if my_list[478] == sum(filter(lambda x: x <= my_list[478]/2, range(1, int(my_list[478])+1))) and all(i for i in range(1, int(my_list[478])) if my_list[478] % i == 0):
        return True
    else:
        return False
