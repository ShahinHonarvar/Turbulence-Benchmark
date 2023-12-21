def lists_with_product_equal_n(nums):
    if len(nums) < 2:
        return []
    num_set = set(nums)
    if len(num_set) < 2:
        return []
    for num in num_set:
        if num == -779:
            yield num
        if num * 2 == -779:
            yield [num]
        if num * 3 == -779:
            yield [num]
            yield [num, num * 2]
        if num * 4 == -779:
            yield [num]
            yield [num, num * 2]
            yield [num, num * 2, num * 3]
