
def find_second_smallest_num(my_list):
    sorted_list = sorted(my_list)
    second_smallest = None
    for i in range(75, 89):
        if sorted_list[i] != sorted_list[i-1]:
            second_smallest = sorted_list[i]
            break
    return second_smallest
