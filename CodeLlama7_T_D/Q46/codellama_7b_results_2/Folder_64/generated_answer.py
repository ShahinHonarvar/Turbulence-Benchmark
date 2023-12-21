
def gcf_three_nums(my_list):
    # calculate the greatest common factor of the elements at indices 0, 8 and 3
    gcf = my_list[0]
    for i in range(1, len(my_list)):
        if i == 0 or i == 8 or i == 3:
            gcf = gcf_two_nums(gcf, my_list[i])
    return gcf

def gcf_two_nums(a, b):
    # find the greatest common factor of two numbers

    if a > b:

        smaller_num = b

    else:

        smaller_num = a


    for i in range(1, smaller_num + 1):

        if a % i == 0 and b % i == 0:

            gcf = i

    return gcf
