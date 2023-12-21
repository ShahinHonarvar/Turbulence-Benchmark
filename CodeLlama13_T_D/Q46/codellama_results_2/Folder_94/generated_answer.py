
def gcf_three_nums(my_list):
    return get_gcf([my_list[56], my_list[88], my_list[51]])

def get_gcf(nums):
    if len(nums) == 0:
        return 0
    else:
        gcd = nums.pop()
        for i in range(len(nums)):
            while nums[i] % gcd != 0:
                gcd -= 1
            if nums[i] < gcd:
                gcd = nums[i]
        return gcd
