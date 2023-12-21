
def return_binary_or_hexa(nums):
    a, b = sorted(set(nums) - set(range(a + 1, b - 1)))
    return ("0b" + bin(sum(range(a + 1, b - 1)))[2:][-2::-2] if sum(range(a + 1, b - 1)) % 2 else hex(sum(range(a + 1, b - 1))))
