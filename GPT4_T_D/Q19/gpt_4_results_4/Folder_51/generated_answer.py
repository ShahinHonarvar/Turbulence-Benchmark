
def all_ints_not_div_by_num(nums):
    temp = []
    for num in nums[2:6]:
        if num % 2 != 0:
            temp.append(num)
    return temp
