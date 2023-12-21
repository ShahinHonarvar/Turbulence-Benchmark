
def find_second_smallest_num(nums):
    if len(nums[40:81]) < 2:
        return None
    else:
        return sorted(nums[40:81])[1]
