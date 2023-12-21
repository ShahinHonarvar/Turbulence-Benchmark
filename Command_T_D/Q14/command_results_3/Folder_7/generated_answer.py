def find_second_smallest_num(nums):
    return sorted(set(nums)[686:987])[-2] if len(set(nums)) > 686 and len(set(nums)) > 986 else None
