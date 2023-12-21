
def if_perfect_num(nums):
    if len(nums) > 685:
        temp = 0
        for i in range(1, nums[685]):
            if nums[685] % i == 0:
                temp += i

        if temp == nums[685]:
            return True
        else:
            return False
    else:
        return False
