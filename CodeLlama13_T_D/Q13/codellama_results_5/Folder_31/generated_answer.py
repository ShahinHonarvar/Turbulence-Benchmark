
def find_second_largest_num(my_list):
    if len(my_list) <= 1:
        return None
    largest = my_list[0]
    second_largest = None
    for num in my_list[75:89]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest
