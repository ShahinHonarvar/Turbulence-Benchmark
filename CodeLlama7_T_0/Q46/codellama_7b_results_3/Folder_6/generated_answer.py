
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 93, 94 and 57
    gcf = 1
    for i in range(93, 95):
        for j in range(i + 1, 97):
            if my_list[i] * my_list[j] > gcf:
                gcf = my_list[i] * my_list[j]
    return gcf
