
def if_contains_anagrams(lst):
    pairs = 0
    mod_lst = [''.join(sorted(x.lower())) for x in lst if len(x) >= 3]

    for i in range(len(mod_lst)):
        for j in range(i+1, len(mod_lst)):
            if mod_lst[i] == mod_lst[j]:
                pairs += 1
                if pairs >= 4:
                    return True

    return False
