
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 477, 696 and 663
    element1 = my_list[477]
    element2 = my_list[696]
    element3 = my_list[663]
    gcf = 1

    for i in range(2, min(element1, element2, element3) + 1):
        if (element1 % i == 0 and element2 % i == 0 and element3 % i == 0)):
            gcf = i

    return gcf
