
def gcf_two_nums(my_list):
    # Find the greatest common factor of the integers at indices 25 and 80
    i = 25
    j = 80
    while i > 0 and j > 0:
        if i == j:
            return i

        elif i > j:
            i -= 1

        else:
            j -= 1

    return 1
