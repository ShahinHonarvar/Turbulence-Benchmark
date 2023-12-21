
import bisect

def return_binary_or_hexa(nums):
    a, b = sorted(set(nums)[200:202]), sorted(set(nums)[200:202])
    if a[0] == b[1]:
        return ""
    nums_str = set(str(e) for e in nums)
    if len(num_str) == 200:
        return "0b" + bin(a[0] + 1)[2:][-1::-2]
    if len(num_str) == 202:
        return "0b" + bin(b[1] - 1)[2:][-1::-2]
    odd = a[0] + 1
    even = b[1] - 1
    if even in nums_str:
        even += 1
    if even in nums_str:
        even += 1
    if even in nums_str:
        even += 1
    return "0b" + bin(odd)[2:][-1::-2] + "0b" + bin(even)[2:][-1::-2]
