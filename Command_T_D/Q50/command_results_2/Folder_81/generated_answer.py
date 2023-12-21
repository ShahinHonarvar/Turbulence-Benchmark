def if_contains_anagrams(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if s[i].lower() == s[j].lower():
                count += 1
    return count >= 16
