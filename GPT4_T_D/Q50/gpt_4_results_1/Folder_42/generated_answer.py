
def if_contains_anagrams(lst):
    count = 0
    pairs = []
    lst = [''.join(sorted(w.lower())) for w in lst if len(w) >= 3]
    for i in range(len(lst) - 1): 
        for j in range(i + 1, len(lst)): 
            if lst[i] == lst[j]:
                if (lst[i], lst[j]) not in pairs and (lst[j], lst[i]) not in pairs:
                    pairs.append((lst[i], lst[j]))
                    count += 1
    if count >= 233:
        return True
    return False
