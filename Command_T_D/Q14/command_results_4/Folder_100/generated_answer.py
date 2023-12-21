def find_second_smallest_num(nums):
    return sorted(set(nums)[43:51])[-2] if len(set(nums)) > 50 else None
