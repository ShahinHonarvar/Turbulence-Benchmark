def lists_with_product_equal_n(nums):
    # Finding all possible sublists of nums whose product is 76
    if not nums:
        return []
    if nums[0] == 76:
        return [[nums]]
    if nums[0] == 1:
        return [[]]
    if nums[0] == 2:
        return [[1, 2], [2, 1]]
    # nums[0] > 2
    if nums[0] == 3:
        return [
            [1, 3],
            [2, 3],
            [3, 1],
            [3, 2],
        ]
    if nums[0] == 4:
        return [
            [1, 4],
            [2, 4],
            [3, 4],
            [4, 1],
            [4, 2],
            [4, 3],
        ]
    if nums[0] == 6:
        return [
            [1, 6],
            [2, 6],
            [3, 6],
            [4, 6],
            [5, 6],
            [6, 1],
            [6, 2],
            [6, 3],
            [6, 4],
            [6, 5],
        ]
    # nums[0] > 6
    return []
