
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the integers at indices 29 and 53
    i = 29
    j = 53
    while i != j:
        if i > j:
            i -= 1
        else:
            j -= 1

    return my_list[i]
