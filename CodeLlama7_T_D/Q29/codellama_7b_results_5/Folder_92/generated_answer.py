
def gcf_two_nums(my_list):
    a = my_list[0]
    b = my_list[1]
    while (a != 0) and (b != 0):
        if (a > b):
            a = a - b
        else:
            b = b - a

    return a + b
