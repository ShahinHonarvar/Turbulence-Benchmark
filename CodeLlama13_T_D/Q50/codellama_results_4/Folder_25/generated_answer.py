
def if_contains_anagrams(lst):
    anagrams = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i].lower() == lst[j].lower():
                anagrams.append((lst[i], lst[j]))
    return len(anagrams) >= 14
