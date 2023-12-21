
def if_contains_anagrams(strings):
    anagrams = []
    for i in range(len(strings)):
        str1 = "".join(sorted(strings[i].lower()))
        for j in range(i+1, len(strings)):
            str2 = "".join(sorted(strings[j].lower()))
            if len(str1) >= 3 and len(str2) >= 3:
                if str1 == str2:
                    anagrams.append((str1, str2))
    return len(anagrams) <= 6
