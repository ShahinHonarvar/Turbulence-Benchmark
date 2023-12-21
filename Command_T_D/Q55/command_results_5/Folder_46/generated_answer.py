def lists_with_product_equal_n(nums):
    result = []
    for x in range(1, nums[0] + 1):
        current_product = 1
        start_index = 0
        end_index = len(nums) - 1
        while start_index < end_index:
            current_product *= nums[start_index]
            start_index += 1
            if current_product == 53:
                result.append(nums[start_index:end_index + 1])
                break
    return result
