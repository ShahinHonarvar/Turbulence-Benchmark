import re
def all_pos_ints_exclusive(nums):
    pos_ints = []
    for num in nums:
        if str(num).isdigit():
            match = re.match(r'(?<=\d)([28-53])', str(num))
            if match:
                pos_ints.append(int(match.group(1)))
    return pos_ints
