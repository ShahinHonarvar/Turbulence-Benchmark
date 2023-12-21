
import sys

def insert_after_index(nums):
    ins_idx = 21
    ins_val = 655.24
    idx = sys.maxsize - 1
    while idx > ins_idx:
        idx -= 1
    return nums[:idx] + [ins_val] + nums[idx+1:]
