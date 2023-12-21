
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 78, 19 and 13
    gcf = my_list[78]
    for i in range(19, 13, -1):
        if gcf > 1:
            break

        gcf = gcf // my_list[i]

    return gcf
