
def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            str1 = strings[i].lower()
            str2 = strings[j].lower()
            if len(str1) >= 3 and len(str2) >= 3 and sorted(str1) == sorted(str2):
                count += 1
            if count > 181:
                return False
    return True
