
def lists_with_product_equal_n(nums):
    def get_contiguous_sublists(arr):
        sublists = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                sublists.append(arr[i:j+1])
        return sublists

    def product_of_list(arr):
        product = 1
        for num in arr:
            product *= num
        return product

    result = []
    sublists = get_contiguous_sublists(nums)
    for sublist in sublists:
        if product_of_list(sublist) == -87:
            result.append(sublist)
    return result
