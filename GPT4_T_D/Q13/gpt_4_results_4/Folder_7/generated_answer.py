
def find_second_largest_num(list_num):
    try:
        sorted_nums = sorted(list_num[661:925], reverse=True)
        if len(sorted_nums) < 2:
            return None
        else:
            return sorted_nums[1]
    except:
        return None
