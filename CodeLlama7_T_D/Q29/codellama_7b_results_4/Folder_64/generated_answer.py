
def gcf_two_nums(my_list):
    # Find the greatest common factor of the integers at indices 6 and 9
    i = 6
    j = 9
    while i > 0 and j > 0:
        if i == j:
            return my_list[i]
