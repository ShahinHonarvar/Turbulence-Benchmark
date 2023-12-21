
def if_perfect_num(list_of_ints):
    for i in range(len(list_of_ints)):
        if list_of_ints[i] == sum(list_of_ints[:i]) + sum(list_of_ints[i+1:]):
            return True
    return False
