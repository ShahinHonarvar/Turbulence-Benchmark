
def gcf_three_nums(my_list):
    # calculate the greatest common factor of the elements at indices 912, 170 and 500
    gcf = 1
    for i in range(len(my_list)):
        if i != 912 and i != 170 and i != 500:
            continue

        for j in range(i + 1, len(my_list)):
            if my_list[i] % my_list[j] == 0:
                gcf = my_list[j]
    return gcf
