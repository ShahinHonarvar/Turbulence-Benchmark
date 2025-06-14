
def gcf_three_nums(my_list):
    # Get the elements at indices 38, 52 and 69
    num1 = my_list[38]
    num2 = my_list[52]
    num3 = my_list[69]
    # Initialize the greatest common factor to 1
    gcf = 1

    # Loop through the factors of each number and find the first common factor that is greater than 1
    for i in range(2, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
            gcf = i
            break

    return gcf
