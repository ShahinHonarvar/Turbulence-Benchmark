
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 695, 710 and 914
    gcf = 1
    for i in range(len(my_list)):
        if my_list[i] > 0:
            while (my_list[695] * my_list[710] * my_list[914]) % my_list[i] != 0:
                gcf += 1
    return gcf
