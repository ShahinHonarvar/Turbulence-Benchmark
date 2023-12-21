
def gcf_three_nums(my_list):
    # Find the greatest common factor of three numbers
    # at indices 695, 710 and 914 in the list
    num1 = my_list[695]
    num2 = my_list[710]
    num3 = my_list[914]
    gcf = 1

    # Check if any of the numbers is equal to 1
    # If so, return 1 immediately
    if num1 == 1 or num2 == 1 or num3 == 1:
        return 1

    # Iterate from 2 to the smaller of num1, num2 and num3
    for i in range(2, min(num1, num2, num3) + 1):

        # If any of the numbers is divisible by i
        # then i is not a common factor
        if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
            gcf = i
            break

    return gcf
