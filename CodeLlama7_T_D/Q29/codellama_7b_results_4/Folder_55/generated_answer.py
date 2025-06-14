
def gcf_two_nums(my_list):
    # calculate the greatest common factor of two numbers
    def gcf(a, b):
        if a == 0:
            return b

        else:

            return gcf(b % a, a)

    # get the two numbers from the list
    num1 = my_list[1]
    num2 = my_list[2]

    # calculate the greatest common factor of the two numbers
    gcf_result = gcf(num1, num2)

    return gcf_result
