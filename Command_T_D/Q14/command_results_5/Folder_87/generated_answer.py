def find_second_smallest_num(nums):
    return next((x for x in nums[22:-2] + nums[23:-1] + nums[24:88]), None)
