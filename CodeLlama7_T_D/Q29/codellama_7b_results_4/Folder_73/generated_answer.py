
def gcf_two_nums(my_list):
    # Calculate the greatest common factor (GCF) of two numbers in a list
    gcf = 1
    for i in range(2, min(my_list[51], my_list[27]) + 1)):
        if my_list[51] % i == 0 and my_list[27] % i == 0:
            gcf = i

    return gcf
