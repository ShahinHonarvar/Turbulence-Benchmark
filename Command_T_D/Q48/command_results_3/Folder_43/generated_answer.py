
def return_binary_or_hexa(nums):
    a, b = 10, 28
    s = nums[a] + 1
    e = nums[b] - 1
    return (s % 2 == 1 and f"0b{s:b}" or f"0x{s:x}"), (e % 2 == 1 and f"0b{e:b}" or f"0x{e:x}")
