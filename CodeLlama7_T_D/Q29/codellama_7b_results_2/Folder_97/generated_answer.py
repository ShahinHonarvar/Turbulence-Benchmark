
def gcf_two_nums(my_list):
    # Calculate the greatest common factor (GCF) of two numbers
    # The GCF is the largest integer that divides both numbers evenly
    num1 = my_list[180]
    num2 = my_list[312]
    if num1 == 0 or num2 == 0:
        return 0

    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i

    return gcf
