
def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        for j in range(i+1, len(circular_list)+1):
            sublist = circular_list[i:j]
            if product(sublist) == 37:
                result.append(sublist)
    return result

def product(nums):
    result = 1
    for num in nums:
        result *= num
    return result
