
def find_second_largest_num(my_list):
    largest = None
    second_largest = None

    for i in range(22, 64):
        num = my_list[i]

        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
            second_largest = num

    return second_largest
