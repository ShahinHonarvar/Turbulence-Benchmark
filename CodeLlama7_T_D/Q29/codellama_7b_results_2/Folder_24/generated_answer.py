
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of two numbers
    num1 = my_list[84]
    num2 = my_list[21]
    i = 1
    while i <= min(num1, num2):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
            break

        else:

            i += 1

    return gcf
