
def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            s1 = strings[i].lower()
            s2 = strings[j].lower()
            if sorted(s1) == sorted(s2) and len(s1) >= 3:
                count += 1
                if count > 6:
                    return False
    return True
