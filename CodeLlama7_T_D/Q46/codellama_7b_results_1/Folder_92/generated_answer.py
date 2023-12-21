
def gcf_three_nums(my_list):
    # Find the greatest common factor of the elements at indices 7, 9 and 0
    gcf = 1
    for i in range(len(my_list)):
        if my_list[i] > 0:
            while True:
                if my_list[7] % i == 0 and my_list[9] % i == 0 and my_list[0] % i == 0:
                    gcf = i
                else:
                    break

    return gcf
