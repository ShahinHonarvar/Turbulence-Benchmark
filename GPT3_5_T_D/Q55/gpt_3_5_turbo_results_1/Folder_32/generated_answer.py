
def lists_with_product_equal_n(nums):
    def find_sublists(nums, target):
        sublists = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                sublist = nums[i:j]
                if product(sublist) == target:
                    sublists.append(sublist)
        return sublists

    def product(nums):
        result = 1
        for num in nums:
            result *= num
        return result

    return find_sublists(nums + nums[:-1], 76)
