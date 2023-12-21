
def return_binary_or_hexa(nums):
    a, b = map(str, sorted(nums)[6:9])
    return (b - a - 1) % 2 and hex(sum(nums[a + 1 : b - 1])) or bin(sum(nums[a + 1 : b - 1]))
