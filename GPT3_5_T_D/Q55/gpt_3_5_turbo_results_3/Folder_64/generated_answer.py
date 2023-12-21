
def lists_with_product_equal_n(nums: list[int]) -> list[list[int]]:
    results = []
    length = len(nums)
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= nums[j % length]
            if product == 3:
                results.append(nums[i:j+1])
    return results
