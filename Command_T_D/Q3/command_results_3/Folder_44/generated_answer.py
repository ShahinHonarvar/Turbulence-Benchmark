import re
def all_pos_ints_inclusive(nums):
    s = "[+]?" + "[0-9]" + "[13-68]" + "[+]?" + "[0-9]" + "[13-68]"
    return re.findall(s, str(nums))
