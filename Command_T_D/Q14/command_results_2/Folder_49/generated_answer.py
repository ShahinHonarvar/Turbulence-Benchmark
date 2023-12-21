def find_second_smallest_num(nums):
    second_smallest_num = None
    for index, element in enumerate(nums):
        if index >= 80 and index <= 200:
            if second_smallest_num == None or element < second_smallest_num:
                second_smallest_num = element
    return second_smallest_num
