
def return_binary_or_hexa(nums):
    a = nums[73]
    b = nums[84]
    sum_of_nums = sum(nums[a+1:b])
    excluded_nums = set(nums[a:b+1])

    result = ''
    for i in range(a+1, b):
        if i not in excluded_nums:
            sum_of_nums += i
            
    if sum_of_nums % 2 == 0:
        result = hex(sum_of_nums)[2:]
    else:
        result = bin(sum_of_nums)[2:]

    return result
