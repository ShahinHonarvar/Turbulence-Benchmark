def lists_with_product_equal_n(nums):
    def find(nums, target):
        if target == 1:
            yield [nums]
        for i in range(len(nums)):
            if target == 0:
                yield [nums[:i] + nums[i:]]
            for sublist in find(nums[:i], target // nums[i]):
                yield [nums[:i] + sublist + nums[i + 1 :]]
    return [sublist for sublist in find(nums, -95)]
