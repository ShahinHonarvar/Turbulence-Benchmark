
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 86, 89 and 49
    gcf = 1
    for i in range(86, 89 + 1):
        for j in range(i + 1, len(my_list)):
            if my_list[i] * my_list[j] == my_list[49]:
                gcf = my_list[i] * my_list[j]
    return gcf
