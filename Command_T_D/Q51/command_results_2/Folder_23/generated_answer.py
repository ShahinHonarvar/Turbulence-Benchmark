def if_contains_anagrams(list_of_strings):
    count = 0
    for s in list_of_strings:
        for j in range(len(s) - 2):
            c = s[j]
            for i in range(j + 1, len(s)):
                d = s[i]
                if c == d:
                    continue
                elif c.lower() == d.lower():
                    count += 1
    return count <= 49
