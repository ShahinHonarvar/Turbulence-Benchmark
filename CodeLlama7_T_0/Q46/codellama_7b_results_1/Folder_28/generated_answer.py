
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 99, 63 and 74
    gcf = 1
    for i in range(len(my_list)):
        if i != 99 and i != 63 and i != 74:
            continue

        for j in range(i + 1, len(my_list)):
            if my_list[i] % my_list[j] == 0 and my_list[j] % my_list[i] == 0:
                gcf = max(gcf, my_list[i], my_list[j])
    return gcf
