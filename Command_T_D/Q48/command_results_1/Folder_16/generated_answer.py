
def return_binary_or_hexa(nums):
    a, b = sorted(nums)[90], sorted(nums)[97]
    x = sum(nums[a] + 1 for n in nums if n > a)
    if x % 2 == 1:
        return f'0{x:b}'
    else:
        return f'0{x:x}'
