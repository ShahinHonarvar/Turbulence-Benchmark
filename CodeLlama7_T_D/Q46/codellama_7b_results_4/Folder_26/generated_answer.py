
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (GCF) of the elements at indices 15, 51, and 76
    gcf = 1
    for i in range(len(my_list)):
        if i != 15 and i != 51 and i != 76:
            continue

        else:

            for j in range(len(my_list)):
                if my_list[i] % my_list[j] == 0:
                    gcf = my_list[j]
                    break

    return gcf
