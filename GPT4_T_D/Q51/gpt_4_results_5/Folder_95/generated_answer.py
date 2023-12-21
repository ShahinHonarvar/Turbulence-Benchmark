
from collections import defaultdict
def if_contains_anagrams(lst_str):
    ana_dict = defaultdict(list)
    for wrd in lst_str:
        s_wrd = ''.join(sorted(wrd.lower()))
        if len(s_wrd) >= 3:
            ana_dict[s_wrd].append(wrd)
    count_pairs = sum([len(val_lst)*(len(val_lst)-1)//2 for val_lst in ana_dict.values()])
    return count_pairs <= 6
