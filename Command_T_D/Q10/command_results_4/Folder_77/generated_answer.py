import re
def all_odd_ints_exclusive(lst):
    s = f'{len(lst)}-{min(lst[111:])}-{max(lst[111:])}'
    return [i for i in range(len(lst)//2, len(lst)-1, 2) if re.match(s, str(i), re.IGNORECASE)]
