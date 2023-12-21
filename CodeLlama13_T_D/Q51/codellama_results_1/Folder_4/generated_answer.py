
def if_contains_anagrams(strings):
    for i, s in enumerate(strings):
        for j in range(i+1, len(strings)):
            if sorted(s.lower()) == sorted(strings[j].lower()):
                return True
    return False
