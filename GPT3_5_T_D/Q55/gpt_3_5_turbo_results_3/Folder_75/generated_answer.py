
def lists_with_product_equal_n(circular_list):
    def get_product(nums):
        product = 1
        for num in nums:
            product *= num
        return product

    size = len(circular_list)
    result = []
    
    for i in range(size):
        sublist = []
        for j in range(size):
            sublist.append(circular_list[(i+j)%size])
            product = get_product(sublist)
            if product == 13:
                result.append(sublist)
            elif product > 13:
                break
    
    return result
