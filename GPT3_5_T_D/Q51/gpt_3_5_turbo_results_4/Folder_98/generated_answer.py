
def if_contains_anagrams(strings):
    count = 0
    for i, s1 in enumerate(strings):
        for j, s2 in enumerate(strings):
            if i != j and sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3:
                count += 1
                if count > 46:
                    return False
    return True
