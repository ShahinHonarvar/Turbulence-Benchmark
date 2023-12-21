def if_perfect_num(list_of_ints):
    return list_of_ints[42] == sum(list_of_ints[:42]) == sum(list_of_ints[42:])
