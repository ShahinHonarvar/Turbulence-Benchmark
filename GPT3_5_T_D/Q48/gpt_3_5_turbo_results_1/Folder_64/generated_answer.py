
def return_binary_or_hexa(nums):
    a = nums[0]
    b = nums[5]
    sum = 0
    for num in range(a+1, b):
        if num not in nums[1:5]:
            sum += num
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
