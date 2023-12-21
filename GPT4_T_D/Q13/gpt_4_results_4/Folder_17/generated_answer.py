
def find_second_largest_num(list_of_nums):
    if len(list_of_nums) < 79:
        return None
    else:
        sorted_list = sorted(list_of_nums[62:79], reverse=True)
        if len(sorted_list) < 2:
            return None
        else:
            return sorted_list[1]
