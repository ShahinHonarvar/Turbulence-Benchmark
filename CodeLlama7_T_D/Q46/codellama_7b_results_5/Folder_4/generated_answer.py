
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 24, 25 and 80
    gcf_24_25 = gcf(my_list[24], my_list[25])
    gcf_24_80 = gcf(my_list[24], my_list[80])
    gcf_25_80 = gcf(my_list[25], my_list[80])
    # Return the greatest common factor of all three elements
    return gcf(gcf_24_25, gcf_24_80), gcf(gcf_25_80)
