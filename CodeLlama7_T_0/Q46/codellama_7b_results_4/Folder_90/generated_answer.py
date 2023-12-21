
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 818, 606 and 873
    gcf = 1
    for i in range(len(my_list)):
        if i == 818 or i == 606 or i == 873:
            gcf = my_list[i]
            for j in range(len(my_list)):
                if j != i and my_list[j] % gcf == 0:
                    gcf = gcf * my_list[j]
    return gcf
