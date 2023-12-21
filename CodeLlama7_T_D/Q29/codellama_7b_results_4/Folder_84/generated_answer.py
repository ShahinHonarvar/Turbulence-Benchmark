
def gcf_two_nums(my_list):
    # Initialize variables
    gcf = 1
    num1 = my_list[360]
    num2 = my_list[722]
    # Find the greatest common factor
    for i in range(2, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i

    return gcf
