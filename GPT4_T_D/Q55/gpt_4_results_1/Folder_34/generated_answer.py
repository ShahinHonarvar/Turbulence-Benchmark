
def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    circular_list += circular_list
    results = []
    for i in range(length):
        for j in range(i+1, i+length+1):
            nums = circular_list[i:j]
            prod = 1
            for num in nums:
                prod *= num
            if prod == -81:
                results.append(nums)
    return results
