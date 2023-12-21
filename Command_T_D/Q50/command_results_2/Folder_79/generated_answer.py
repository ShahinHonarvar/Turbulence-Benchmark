def if_contains_anagrams(s):
    n = len(s)
    m = 40
    if n < m:
        return False
    anagrams = {}
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            str1 = s[i] + s[j]
            str2 = s[i][1:] + s[j][1:]
            if str1 in anagrams:
                anagrams[str1] += 1
            if str2 in anagrams:
                anagrams[str2] += 1
            if anagrams[str1] >= m and anagrams[str2] >= m:
                return True
    return False
