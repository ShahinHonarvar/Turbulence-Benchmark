
def if_contains_anagrams(lst):
    anagrams_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i].lower()) == sorted(lst[j].lower()) and len(lst[i]) >= 3 and len(lst[j]) >= 3:
                anagrams_count += 1
    if anagrams_count >= 73:
        return True
    else:
        return False
