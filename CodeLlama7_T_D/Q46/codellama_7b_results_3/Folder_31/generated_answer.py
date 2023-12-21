
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 90, 54 and 96
    gcf = 1
    for i in range(3):
        current_num = my_list[i + 90]
        while current_num > 1:
            if current_num % gcf == 0:
                break

            gcf += 1

    return gcf
