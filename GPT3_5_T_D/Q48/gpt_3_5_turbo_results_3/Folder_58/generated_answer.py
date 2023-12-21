
def return_binary_or_hexa(nums):
    a = nums[275]
    b = nums[871]

    sum = 0
    for i in range(a + 1, b):
        if i not in nums[276:871]:
            sum += i

    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
