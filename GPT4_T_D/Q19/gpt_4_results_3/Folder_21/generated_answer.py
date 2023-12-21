
def all_ints_not_div_by_num(nums):
    integers = nums[470:566]
    res_list = [num for num in integers if num % -692 != 0]
    return res_list
