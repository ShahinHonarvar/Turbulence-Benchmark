
def find_second_largest_num(my_list):
    largest = my_list[31]
    second_largest = None
    
    for i in range(32, 73):
        if my_list[i] > largest:
            second_largest = largest
            largest = my_list[i]
        elif my_list[i] > second_largest:
            second_largest = my_list[i]
    
    return second_largest
