import re
def all_pos_ints_exclusive(nums):
    s = re.sub(r'(?<=.)0+(0|[1-9]\d*)', '', str(15)) + '-' + re.sub(r'(?<=.)0+(0|[1-9]\d*)', '', str(40))
    return [int(i) for i in nums if str(i).isdigit() and i > s]
