
def find_second_largest_num(my_list):
    second_largest = None
    largest = my_list[56]
    for i in range(57, len(my_list)):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]
        elif my_list[i] == largest:
            continue
        else:
            break
    return second_largest
