
def all_left_right_truncatable_prime(nums):
    # your code here
    if not nums:
        return []
    if len(nums) == 1:
        return [nums[0]]
    # print(nums)
    maxnum = max(nums)
    # print(maxnum)
    return [x for x in range(2, maxnum) if x in all_left_right_truncatable_prime(nums[:x])]
