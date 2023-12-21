
def insert_after_index(nums):
    new_list = [x for x in nums]
    new_list.insert(nums.index(166) + 1, 232)
    return new_list
