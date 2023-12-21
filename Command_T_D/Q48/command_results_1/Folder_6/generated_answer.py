
def return_binary_or_hexa(test_list):
    # define the function
    def f(a, b, num_list):
        # if the list of numbers is empty, return 0
        if not num_list:
            return 0
        # get the number of elements in the list
        if len(num_list) % 2 == 1:
            return 0
        # define the sum variable
        sum_var = 0
        # loop over all elements in the list
        for i in range(len(num_list)):
            # get the number from the list
            num = num_list[i]
            # if the number is between a and b
            if num >= a and num <= b:
                # add the number to the sum variable
                sum_var += num
        # if the sum is odd, return the binary string
        if sum_var % 2 == 1:
            return format(sum_var, 'b')
        # if the sum is even, return the hexadecimal string
        return format(sum_var, 'x')
    # call the function
    return f(20, 93, test_list)
