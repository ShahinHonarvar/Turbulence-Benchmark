
def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        lowercase_s = s.lower()
        anagrams += [(i, j) for i in range(len(lowercase_s)) for j in range(i+3, len(lowercase_s)) if sorted(lowercase_s[i:j]) == sorted(lowercase_s[j:i])]
    return len(anagrams) <= 15
