
def if_perfect_num(my_list):
    return my_list[537] == sum(set([j for j in range(1, int(my_list[537])**0.5+1) if my_list[537] % j == 0]))
