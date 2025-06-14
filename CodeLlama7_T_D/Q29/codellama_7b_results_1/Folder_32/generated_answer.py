
def gcf_two_nums(my_list):
    # Get the greatest common factor of the integers at indices 47 and 22
    return gcf(my_list[47], my_list[22])
# Helper function to find the greatest common factor of two numbers
def gcf(a, b):
    if a == 0:
        return b

    while a != b:

        if a > b:
            a = a - b
        else:
            b = b - a

    return a
