
def if_contains_anagrams(lst):
    pairs = []
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    pairs.append((lst[i], lst[j]))
    return len(pairs) >= 123
