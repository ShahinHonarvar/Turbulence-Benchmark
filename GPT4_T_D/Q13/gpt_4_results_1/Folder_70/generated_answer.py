
def find_second_largest_num(num_list):
    try:
        relevant_nums = num_list[28:33]
        if not relevant_nums:
            return None
        relevant_nums.sort()
        return relevant_nums[-2]
    except IndexError:
        return None
