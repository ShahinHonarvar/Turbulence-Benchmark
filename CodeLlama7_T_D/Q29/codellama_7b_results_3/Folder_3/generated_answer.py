
def gcf_two_nums(my_list):
    # find the greatest common factor of the integers at indices 47 and 10
    i = 47
    j = 10
    while i > 0 and j > 0:
        if i % 2 == 0 and j % 2 == 0:
            i //= 2
            j //= 2
        else:
            if i % 2 == 0:
                i //= 2

            elif j % 2 == 0:
                j //= 2
            else:
                if i > j:
                    i -= j
                else:
                    j -= i

    return i if i > 0 else j
