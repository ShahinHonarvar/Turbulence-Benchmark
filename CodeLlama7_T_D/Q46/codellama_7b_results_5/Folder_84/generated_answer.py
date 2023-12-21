
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 695, 710 and 914
    gcf = 1
    for i in range(695, 710):
        for j in range(i + 1, len(my_list)):
            if my_list[i] * my_list[j] <= my_list[695] * my_list[710] * my_list[914]:
                gcf = max(gcf, my_list[i] * my_list[j])
    return gcf
