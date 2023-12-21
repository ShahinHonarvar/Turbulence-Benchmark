
def if_contains_anagrams(lst):
    counter = 0
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and sorted(lst[i].lower()) == sorted(lst[j].lower()):
                if (lst[i], lst[j]) not in pairs and (lst[j], lst[i]) not in pairs:
                    pairs.append((lst[i], lst[j]))
    if len(pairs) >= 95:
        return True
    else:
        return False
