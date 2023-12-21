
def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        string1 = strings[i].lower()
        if len(string1) >= 3:
            for j in range(i+1,len(strings)):
                string2 = strings[j].lower()
                if len(string2) >= 3 and sorted(string1) == sorted(string2):
                    count += 1
                    if count > 9:
                        return False
    return True
