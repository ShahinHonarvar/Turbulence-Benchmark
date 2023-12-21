
def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        str1 = strings[i].lower()
        for j in range(i+1, len(strings)):
            str2 = strings[j].lower()
            if sorted(str1) == sorted(str2) and len(str1) >= 3:
                count += 1
                if count >= 42:
                    return True
    return False
