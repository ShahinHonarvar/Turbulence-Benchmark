
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 66, 56 and 92
    gcf = 1
    for i in range(66, 93):
        if my_list[i] % gcf == 0:
            continue

        else:

            while my_list[66] * my_list[56] * my_list[92] % my_list[i] != 0:
                gcf += 1
    return gcf
