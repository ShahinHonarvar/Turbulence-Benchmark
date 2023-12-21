
def if_perfect_num(my_list):
    return my_list[746] == sum(filter(lambda x: x < my_list[746] and my_list[746] % x == 0, range(1, int(my_list[746]) ** 0.5 + 1)))
