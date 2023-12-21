
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of two numbers
    a = my_list[4]
    b = my_list[0]
    while True:
        if a == 0 or b == 0:
            break

        if a > b:

            a = a % b

        else:

            b = b % a

    return a
