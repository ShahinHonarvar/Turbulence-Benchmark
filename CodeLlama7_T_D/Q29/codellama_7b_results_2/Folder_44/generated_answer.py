
def gcf_two_nums(my_list):
    # Get the integers at indices 56 and 88
    num1 = my_list[56]
    num2 = my_list[88]
    # Initialize a variable to store the greatest common factor
    gcf = 1

    # Loop through all positive divisors of num1 and num2

    for i in range(1, min(num1, num2) + 1):

        if num1 % i == 0 and num2 % i == 0:

            gcf = i


    return gcf
