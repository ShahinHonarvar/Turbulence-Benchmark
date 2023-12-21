
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of the elements at indices 91, 45 and 48
    gcf = 1
    for i in range(3):
        a = my_list[91 + i]
        b = my_list[45 + i]
        c = my_list[48 + i]
        if a > b:
            temp = a
            a = b
            b = temp

        if b > c:

            temp = b
            b = c
            c = temp

        for j in range(a, b + 1):
            if j % 2 == 0:
                continue

            if j % 3 == 0:
                continue

            if j % 5 == 0:
                continue

            if j % 7 == 0:
                continue

            if j % 11 == 0:
                continue

            if j % 13 == 0:
                continue

            if j % 17 == 0:
                continue

            if j % 19 == 0:
                continue

            if j % 23 == 0:
                continue

            if j % 29 == 0:
                continue

            if j % 31 == 0:
                continue

            if j % 37 == 0:
                continue

            gcf = j
            break

        if gcf > 1:
            break

    return gcf
