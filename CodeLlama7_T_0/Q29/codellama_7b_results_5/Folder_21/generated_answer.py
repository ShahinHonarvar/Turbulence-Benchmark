
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the two numbers
    gcf = 1
    for i in range(2, min(my_list[198], my_list[212]) + 1)):
        if my_list[198] % i == 0 and my_list[212] % i == 0:
            gcf = i
    return gcf
