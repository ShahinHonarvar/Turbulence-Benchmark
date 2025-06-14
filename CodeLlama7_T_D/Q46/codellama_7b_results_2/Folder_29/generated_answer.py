
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 22, 97 and 64
    index1 = my_list[22]
    index2 = my_list[97]
    index3 = my_list[64]
    gcf = 1

    for i in range(2, min(index1, index2, index3) + 1):
        if (index1 % i == 0) and (index2 % i == 0) and (index3 % i == 0)):
            gcf = i
            break

    return gcf
