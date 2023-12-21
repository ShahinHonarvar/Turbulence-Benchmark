
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 876, 203 and 100
    gcf = 1
    for i in range(876, 1000, 1):
        if my_list[i] > 1:
            for j in range(i + 1, 1000, 1):
                if my_list[j] % my_list[i] == 0:
                    gcf = my_list[i]
    return gcf
