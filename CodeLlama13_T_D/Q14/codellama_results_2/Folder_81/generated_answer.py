
def find_second_smallest_num(numbers):
    sorted_nums = sorted(numbers)
    for i in range(10, 100+1):
        if sorted_nums[i] == sorted_nums[i-1]:
            return None
    return sorted_nums[10:100+1][1]
