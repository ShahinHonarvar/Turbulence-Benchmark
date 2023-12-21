def if_contains_anagrams(s):
    cnt = 0
    for i in range(0, len(s) - 2):
        for j in range(i + 1, len(s) - 1):
            tmp = s[i].lower() + s[j].lower()
            for k in range(j + 1, len(s)):
                if s[k].lower() in tmp:
                    break
            else:
                tmp = s[i].lower() + s[j].lower()
                for k in range(j + 1, len(s)):
                    if s[k].lower() in tmp:
                        break
                else:
                    cnt += 1
    return cnt <= 416
