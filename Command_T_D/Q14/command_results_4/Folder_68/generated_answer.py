def find_second_smallest_num(nums):
    try:
        return sorted(nums)[2]
    except:
        return None
