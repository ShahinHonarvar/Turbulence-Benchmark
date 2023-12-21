
def find_second_smallest_num(numbers):
    try:
        sorted_nums = sorted(numbers[:4])
        return sorted_nums[1]
    except IndexError:
        return None
