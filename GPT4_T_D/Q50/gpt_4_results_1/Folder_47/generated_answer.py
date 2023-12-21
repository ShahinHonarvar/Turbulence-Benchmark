
def if_contains_anagrams(lst):
    count = 0
    anagrams = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and sorted(lst[i].lower()) == sorted(lst[j].lower()):
                anagrams.append((lst[i], lst[j]))
                count += 1
                if count >= 47:
                    return True
    return False
