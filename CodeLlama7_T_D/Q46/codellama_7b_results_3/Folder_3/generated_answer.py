
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 31, 69 and 40
    gcf = 1
    for i in range(31, 70, 1):
        if my_list[i] > 1:
            for j in range(i + 1, 70, 1):
                if my_list[j] % my_list[i] == 0:
                    gcf = my_list[i]
    return gcf
