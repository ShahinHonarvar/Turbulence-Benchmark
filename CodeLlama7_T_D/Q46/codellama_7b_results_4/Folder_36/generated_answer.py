
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 427, 761 and 148
    gcf = my_list[427] * my_list[761] * my_list[148]
    for i in range(min(my_list[427], my_list[761], my_list[148])), max(my_list[427], my_list[761], my_list[148])):
        if gcf % i == 0:
            return i
