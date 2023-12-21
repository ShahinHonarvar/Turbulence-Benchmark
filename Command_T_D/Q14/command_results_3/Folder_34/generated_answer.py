def find_second_smallest_num(lst):
    sm = min(lst)
    smi = sorted(lst)[60:200]
    smj = smi[0]
    smj = smj if smj != sm else smi[1]
    return smj
