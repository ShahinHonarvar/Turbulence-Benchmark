
def if_contains_anagrams(list):
    anagrams = []
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if ''.join(sorted(list[i].lower())) == ''.join(sorted(list[j].lower())):
                anagrams.append((list[i], list[j]))
    return len(anagrams) <= 10
