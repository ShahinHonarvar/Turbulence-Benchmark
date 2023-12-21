 
def lists_with_product_equal_n(nums):
    if nums == []:
        return []
    num_set = set(nums)
    if len(num_set) < 10:
        return []
    max_nums = [i for i in range(10, 0, -1)]
    for num in num_set:
        if num in max_nums:
            if all(num_set[i] == num for i in range(num_set.index(num) + 1)):
                yield num_set[num_set.index(num) + 1:]
                break
