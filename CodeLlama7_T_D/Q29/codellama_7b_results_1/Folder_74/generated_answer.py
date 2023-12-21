
def gcf_two_nums(my_list):
    # Find the greatest common factor of the two numbers at indices 36 and 85
    num1 = my_list[36]
    num2 = my_list[85]
    # Initialize a variable to store the greatest common factor
    gcf = 1

    # Loop through the factors of both numbers

    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i

    return gcf
