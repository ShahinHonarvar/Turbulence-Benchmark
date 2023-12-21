
def insert_at_index(nums):
    lst = list(range(len(nums)))
    lst[70], lst[len(lst) - 1] = 76, lst[70]
    return nums[:70] + [76] + nums[70:-1] + nums[len(lst) - 1:]
