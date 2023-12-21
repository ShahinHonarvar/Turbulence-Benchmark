
def if_contains_anagrams(strings):
    for i, string1 in enumerate(strings):
        for j, string2 in enumerate(strings[i+1:]):
            if len(string1) >= 3 and len(string2) >= 3:
                if sorted(string1.lower()) == sorted(string2.lower()):
                    return True
    return False
