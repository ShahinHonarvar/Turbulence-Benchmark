
def gcf_two_nums(my_list):
    # Find the greatest common factor of two numbers
    # by using the Euclidean algorithm

    a = my_list[84]
    b = my_list[13]

    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if a % greater == 0 and b % greater == 0:
            gcf = greater
            break

        greater -= 1


    return gcf
