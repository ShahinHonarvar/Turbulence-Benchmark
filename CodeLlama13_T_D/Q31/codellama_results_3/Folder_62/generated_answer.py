
def if_perfect_num(list_of_ints):
    return list_of_ints[926] == sum(list_of_ints[:int(list_of_ints[926])**0.5 + 1])
