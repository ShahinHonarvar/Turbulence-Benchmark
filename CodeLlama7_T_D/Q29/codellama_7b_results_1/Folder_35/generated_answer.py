
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the two numbers
    gcf = 1
    for i in range(2, min(my_list[380], my_list[327]) + 1)):
        if my_list[380] % i == 0 and my_list[327] % i == 0:
            gcf = i
    return gcf
