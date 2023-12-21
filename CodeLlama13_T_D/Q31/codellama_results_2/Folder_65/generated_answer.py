
def if_perfect_num(my_list):
    return my_list[35] == sum(filter(lambda x: my_list[35] % x == 0, range(1, int(my_list[35]) ** 0.5 + 1)))
