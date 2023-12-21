
def if_perfect_num(list_of_positive_ints):
    is_perfect = False
    for i in range(851):
        if sum(list_of_positive_ints[:i]) == list_of_positive_ints[i]:
            is_perfect = True
            break
    return is_perfect
