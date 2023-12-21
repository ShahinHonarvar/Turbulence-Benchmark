
def gcf_two_nums(my_list):
    # Calculate the greatest common factor of the integers at indices 23 and 27
    i = 23
    j = 27
    while i > 0 and j > 0:
        if i % 2 == 0 and j % 2 == 0:
            i //= 2
            j //= 2
        elif i % 2 == 1 and j % 2 == 1:
            i += 1
            j += 1
        else:
            break

    return i
