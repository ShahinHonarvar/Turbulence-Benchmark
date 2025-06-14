
def gcf_two_nums(my_list):
    # Find the greatest common factor of the two numbers
    gcf = 1
    for i in range(2, min(my_list[95], my_list[73])) + 1):
        if my_list[95] % i == 0 and my_list[73] % i == 0:
            gcf = i

    return gcf
