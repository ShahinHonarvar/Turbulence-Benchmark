
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers)
    second_smallest = None
    for i in range(25, 88):
        if i == 25:
            continue
        if sorted_nums[i] < sorted_nums[i-1]:
            second_smallest = sorted_nums[i]
            break
    return second_smallest
