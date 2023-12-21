
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 742, 888 and 629
    gcf = 1
    for i in range(len(my_list)):
        if i != 742 and i != 888 and i != 629:
            continue

        for j in range(i + 1, len(my_list)):
            if my_list[i] % my_list[j] == 0:
                gcf = max(gcf, my_list[j])
    return gcf
