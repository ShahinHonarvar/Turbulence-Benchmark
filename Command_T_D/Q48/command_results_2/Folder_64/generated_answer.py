
def return_binary_or_hexa(nums):
    a, b = sorted(nums)[0], sorted(nums)[-1]
    s = sum(i for i in range(a + 1, b - 1) if i not in nums)
    return ("0b" + bin(s).count("1").zfill(len(bin(s))).rstrip("0") if s % 2 else
