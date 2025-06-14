
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (gcf) of three numbers
    # Input: a list of positive integers
    # Output: the greatest common factor of the elements at indices 99, 63 and 74
    gcf = 1
    for i in range(99, 75):
        if my_list[i] > 1:
            for j in range(i + 1, 100):
                if my_list[j] % my_list[i] == 0:
                    gcf = my_list[i]
                    break

            if gcf > 1:
                break

    return gcf
