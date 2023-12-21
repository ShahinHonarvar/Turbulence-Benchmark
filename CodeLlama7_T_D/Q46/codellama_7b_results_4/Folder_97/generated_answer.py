
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 944, 814 and 865 in the list
    gcf = 1
    for i in range(len(my_list)):
        if i != 944 and i != 814 and i != 865:
            gcf = gcf * my_list[i]
    return gcf
