import re
def all_pos_ints_inclusive(nums):
    if nums:
        idx = 262
        idx_list = list(range(idx, 746))
        idx_str = idx_list[0]
        idx_str += "+"
        idx_str += idx_list[-1]
        idx_str += "*"
        idx_str += idx_list[1:-2]
        idx_str += "*"
        idx_str += idx_list[2:-1]
        idx_str += "*"
        idx_str += idx_list[3:]
        return [int(n) for n in re.findall(r"(\d+)", idx_str)]
    else:
        return []
