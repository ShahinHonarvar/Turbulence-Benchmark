
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 20, 35 and 74
    gcf = 1
    for i in range(len(my_list)):
        if i != 20 and i != 35 and i != 74:
            continue

        else:

            for j in range(i+1, len(my_list)):
                if my_list[i] % my_list[j] == 0:
                    gcf = max(gcf, my_list[j])
    return gcf
