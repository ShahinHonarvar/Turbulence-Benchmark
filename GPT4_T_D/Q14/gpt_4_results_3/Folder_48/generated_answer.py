
def find_second_smallest_num(nums):
    try:
        sub_section = nums[246:751]
        sub_section.sort()
        return sub_section[1]
    except IndexError:
        return None
