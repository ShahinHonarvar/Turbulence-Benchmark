def if_contains_anagrams(s):
    res = False
    for i in range(len(s)):
        j = i + 1
        while j < len(s):
            str1 = s[i].lower()
            str2 = s[j].lower()
            if str1 == str2:
                res = True
                break
            elif len(str1) == len(str2):
                if str1 == str2[1:]:
                    res = True
                    break
            j += 1
    return res
