
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of three numbers
    # using the Euclidean algorithm

    a = my_list[24]
    b = my_list[45]
    c = my_list[38]

    if a == 0:
        return b

    elif b == 0:
        return a

    else:

        while True:
            if a % b == 0:
                break

            else:
                temp = a % b
                a = b
                b = temp


        gcf = a
        return gcf
