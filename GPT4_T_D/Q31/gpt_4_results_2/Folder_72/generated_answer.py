
def if_perfect_num(nums):
    if len(nums) > 16:
        num = nums[16]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        if sum == num:
            return True
    return False
