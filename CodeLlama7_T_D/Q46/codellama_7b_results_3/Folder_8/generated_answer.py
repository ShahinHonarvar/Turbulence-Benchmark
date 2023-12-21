
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 99, 28 and 53
    index1 = 99
    index2 = 28
    index3 = 53

    num1 = my_list[index1]
    num2 = my_list[index2]
    num3 = my_list[index3]

    gcf = 1

    for i in range(2, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
            gcf = i

    return gcf
