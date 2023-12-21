
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 40, 15 and 99
    gcf = my_list[40]
    for i in range(15, 99 + 1):
        if gcf == 1:
            break

        else:

            gcf = gcf // math.gcd(gcf, my_list[i])

    return gcf
