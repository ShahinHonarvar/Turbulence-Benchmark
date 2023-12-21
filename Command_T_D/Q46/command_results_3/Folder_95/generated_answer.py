
def gcf_three_nums(nums):
    lst = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] == nums[j] == nums[k]:
                    lst.append(nums[i])
    return max(lst)
