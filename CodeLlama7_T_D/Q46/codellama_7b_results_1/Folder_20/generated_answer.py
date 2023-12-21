
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 29, 53 and 42
    gcf = 1
    for i in range(29, 53):
        for j in range(i + 1, 53):
            if my_list[i] * my_list[j] > gcf:
                gcf = my_list[i] * my_list[j]
    return gcf
