
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 92, 69 and 95
    gcf = 1
    for i in range(len(my_list)):
        if i != 92 and i != 69 and i != 95:
            continue

        for j in range(i + 1, len(my_list)):
            if my_list[i] % my_list[j] == 0:
                gcf = max(gcf, my_list[j])
    return gcf
