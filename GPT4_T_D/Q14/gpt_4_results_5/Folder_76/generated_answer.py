
def find_second_smallest_num(distinct_nums):
    if len(distinct_nums) < 606:
        return None
    slice_data = distinct_nums[533:606]
    slice_data.sort()
    return slice_data[1] if len(slice_data) > 1 else None
