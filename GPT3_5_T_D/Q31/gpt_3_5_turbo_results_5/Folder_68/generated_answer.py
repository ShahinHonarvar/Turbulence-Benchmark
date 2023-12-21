
def if_perfect_num(nums):
    num = nums[3]
    return sum([i for i in range(1, num) if num % i == 0]) == num
