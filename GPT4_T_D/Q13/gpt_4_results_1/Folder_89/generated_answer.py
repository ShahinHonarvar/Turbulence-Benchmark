
def find_second_largest_num(num_list):
    specific_nums = num_list[56:83]
    if len(specific_nums) < 2:
        return None
    else:
        specific_nums.sort()
        return specific_nums[-2]
