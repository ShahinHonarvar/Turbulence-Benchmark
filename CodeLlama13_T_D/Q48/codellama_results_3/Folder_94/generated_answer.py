
def return_binary_or_hexa(nums):
    a, b = 42, 87
    sum_odd = sum([x for x in range(a+1, b) if x not in nums])
    if sum_odd % 2 == 0:
        return hex(sum_odd)[2:]
    else:
        return bin(sum_odd)[2:]
