
def return_binary_or_hexa(nums):
    a, b = 25, 80
    a += 1
    b -= 1
    flag = False
    sum = 0
    for i in range(a, b + 1):
        if i not in nums:
            sum += i
            flag = True
    if flag:
        if sum % 2 == 0:
            return hex(sum)[2:]
        else:
            return bin(sum)[2:]
    else:
        return ""
