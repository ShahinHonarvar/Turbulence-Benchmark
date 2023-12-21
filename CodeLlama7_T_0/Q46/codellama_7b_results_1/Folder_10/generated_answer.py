
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 86, 89 and 49
    gcf = 1
    for i in range(86, 91):
        for j in range(89, 90):
            for k in range(49, 50):
                if my_list[i] * my_list[j] * my_list[k] == gcf:
                    return gcf
                elif my_list[i] * my_list[j] * my_list[k] > gcf:
                    gcf = my_list[i] * my_list[j] * my_list[k]
    return gcf
