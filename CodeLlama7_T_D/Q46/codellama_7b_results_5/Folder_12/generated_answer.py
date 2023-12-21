
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 91, 45 and 48
    gcf = 1
    for i in range(len(my_list)):
        if i != 91 and i != 45 and i != 48:
            continue

        for j in range(i + 1, len(my_list)):
            if my_list[i] % my_list[j] == 0:
                gcf = my_list[j]
    return gcf
