
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 252, 149 and 564
    gcf = 1
    for i in range(3):
        current_gcf = 1
        for j in range(i+1, 3):
            if my_list[j] % my_list[i] == 0:
                current_gcf = my_list[i]
                break

        gcf = max(current_gcf, gcf)

    return gcf
