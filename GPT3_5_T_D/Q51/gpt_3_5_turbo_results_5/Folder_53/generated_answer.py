
def if_contains_anagrams(strings):
    counter = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            str1 = strings[i].lower()
            str2 = strings[j].lower()
            if sorted(str1) == sorted(str2) and len(str1) >= 3:
                counter += 1
                if counter > 8:
                    return False
    return True
