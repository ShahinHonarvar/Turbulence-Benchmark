
def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        for c in range(3, len(s)):
            if len(set(s[:c])) == c and all(set(s[i:i+c]) == set(s[:c]) for i in range(len(s)-c+1)):
                anagrams.append((s, s[i:i+c]))
    return len(anagrams) >= 188
