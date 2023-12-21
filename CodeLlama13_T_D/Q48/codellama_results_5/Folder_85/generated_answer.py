
def return_binary_or_hexa(nums):
    a, b = nums[0], nums[-1]
    sum_of_ints = 0
    for i in range(a+1, b):
        if i not in nums:
            sum_of_ints += i
    if sum_of_ints % 2 == 0:
        return hex(sum_of_ints)[2:]
    else:
        return bin(sum_of_ints)[2:]
