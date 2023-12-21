
def find_second_largest_num(nums):
    result = sorted(nums)[3:5]
    if len(result) == 1:
        return None
    return result[1]
