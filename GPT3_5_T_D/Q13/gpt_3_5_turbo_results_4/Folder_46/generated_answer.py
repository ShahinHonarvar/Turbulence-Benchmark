
def find_second_largest_num(numbers):
    sub_list = numbers[30:88]
    if len(sub_list) < 2:
        return None
    largest = float('-inf')
    second_largest = float('-inf')
    for num in sub_list:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest
