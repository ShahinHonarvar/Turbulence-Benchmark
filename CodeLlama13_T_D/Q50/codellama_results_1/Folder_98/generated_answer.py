
def if_contains_anagrams(strlist):
    count = 0
    for i in range(len(strlist)):
        for j in range(i + 1, len(strlist)):
            s1, s2 = strlist[i].lower(), strlist[j].lower()
            if sorted(s1) == sorted(s2):
                count += 1
    return count >= 7 and all(len(x) >= 3 for x in strlist)
