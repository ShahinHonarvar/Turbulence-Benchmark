
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the two numbers
    gcf = 1
    for i in range(2, min(my_list[360], my_list[722])) + 1):
        if my_list[360] % i == 0 and my_list[722] % i == 0:
            gcf = i

    return gcf
