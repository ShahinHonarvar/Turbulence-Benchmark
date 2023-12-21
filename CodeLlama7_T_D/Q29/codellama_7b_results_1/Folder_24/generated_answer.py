
def gcf_two_nums(my_list):
    # Get the greatest common factor of the integers at indices 84 and 21
    num1 = my_list[84]
    num2 = my_list[21]
    for i in range(min(num1, num2), max(num1, num2)+1)):
        if num1 % i == 0 and num2 % i == 0:
            return i
