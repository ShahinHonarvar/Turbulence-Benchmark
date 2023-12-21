
def return_binary_or_hexa(nums):
    start, end = 18, 52
    nums = sorted(nums)
    missing = []
    for i in range(start+1, end):
        if i not in nums:
            missing.append(i)
    sum = 0
    for i in missing:
        sum += i
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
